from keras.layers import Input
from keras.models import Model, load_model
from keras.optimizers import Adam
import keras.backend as K
import numpy as np
import os
import pickle


laboratory_dict = {
            "engine_speed_mean": 'rpm',
            "Torque_engine_total": "Torque",
            "scavenging_pressure_mean": "scavenging_pressure",
            "fuel_flow_rate_mean": 'fuel_flow_rate',
            "injection_timing_mean": 'injection_timing',
            "exhaust_temperature_mean": 'exhaust_gas_temperature',
            "compression_pressure_mean": 'pressure_compression',
            "firing_pressure_mean": 'max_combustion_pressure',
            "imep_mean": 'mean_effective_pressure',
            "bmep_mean": 'break_mean_effective_presure',
            "break_power_sum": 'break_power',
            "power": 'power',
            "load": 'load',
            "vessel": 'vessel',
            "engine": 'engine'
        }

ui_dict = {v: k for k, v in laboratory_dict.items()}



def get_available_targets():
    available_targets = []
    files = os.listdir("resources/head_models")
    for i in files:
        if (".h5" in i) and ("model" not in i):
            available_targets.append(i[:i.index(".h5")])

    return available_targets


def correct_target(features, predictions, manual_correction):
    inputs1 = []
    inputs2 = []
    for i in features:
        inputs1.append(np.array(i["vggish"]).reshape((5,128)))
        inputs2.append(predictions[-1]["additional_features"][0])

    target = ui_dict[manual_correction["viewed_field"]]

    corrected = np.full((len(features)), float(manual_correction["manual_corrected_value"]))


    try:
        local_trainset = pickle.load(open("resources/head_models/local_" + target + "testset.p", "rb"))
    except:
        local_trainset = [[],[],[]]


    local_trainset = [local_trainset[0] + inputs1, local_trainset[1] + inputs2,local_trainset[2] + corrected.tolist()]


    pickle.dump( local_trainset, open( "resources/head_models/local_" + target + "testset.p", "wb"))

    inputs = [np.array(local_trainset[0]),np.array(local_trainset[1])]
    corrected = np.array(local_trainset[2])


    test_set = pickle.load(open("resources/head_models/"+target+"testset.p", "rb"))

    original_testset = test_set

    test_set = list(test_set)

    test_set[0][0] = np.array(inputs[0].tolist())
    test_set[0][1] = np.array(inputs[1].tolist())
    test_set[1] = np.array(corrected.tolist())


    best_params = {
        "min_original":np.inf,
        "min_new":np.inf

    }
    for lr in [0.1, 0.01, 0.001,0.0001, 0.00001, 0.000001, 0.0000001]:
        for epochs in [1, 4,32,64]:
            for batch_size in [4,16,32,64]:
                target_model = load_model("resources/head_models/" + target + ".h5")
                optimizer = Adam(lr)


                target_model.compile(optimizer=optimizer, loss="mse", metrics=['mae', 'mape'])

                _y_pred_current = target_model.predict(test_set[0]).flatten()
                _y_pred_current_original = target_model.predict(original_testset[0]).flatten()


                target_model.fit(inputs,corrected, epochs = epochs, batch_size=batch_size)

                _y_pred_new = target_model.predict(test_set[0]).flatten()
                _y_pred_original_new = target_model.predict(original_testset[0]).flatten()


                _y_true = test_set[1]

                _y_pred_current_error = np.linalg.norm(_y_pred_current - _y_true)
                _y_pred_current_original_error = np.linalg.norm(_y_pred_current_original - _y_true)

                _y_pred_new_error = np.linalg.norm(_y_pred_new - _y_true)
                _y_pred_new_original_error = np.linalg.norm(_y_pred_original_new - _y_true)


                if (_y_pred_current_error > _y_pred_new_error) and (_y_pred_current_original_error>_y_pred_new_original_error):
                    if (_y_pred_new_error < best_params["min_new"]) and (_y_pred_new_original_error<best_params["min_original"]) :

                        best_params["epochs"] = epochs
                        best_params["lr"] =lr
                        best_params["batch_size"] = batch_size
                        best_params["min_new"] = _y_pred_new_error
                        best_params["original_error"] = _y_pred_current_error
                        best_params["min_original"] = _y_pred_new_original_error


                K.clear_session()




    if "epochs" in best_params:
        target_model = load_model("resources/head_models/" + target + ".h5")
        optimizer = Adam(best_params["lr"])



        target_model.compile(optimizer=optimizer, loss="mse", metrics=['mae', 'mape'])

        _y_pred_current = target_model.predict(test_set[0]).flatten()
        _y_pred_current_original = target_model.predict(original_testset[0]).flatten()

        target_model.fit(inputs, corrected, epochs=best_params["epochs"],batch_size=best_params["batch_size"])

        _y_pred_new = target_model.predict(test_set[0]).flatten()
        _y_pred_original_new = target_model.predict(original_testset[0]).flatten()

        _y_true = test_set[1]

        _y_pred_current_error = np.linalg.norm(_y_pred_current - _y_true)
        _y_pred_current_original_error = np.linalg.norm(_y_pred_current_original - _y_true)

        _y_pred_new_error = np.linalg.norm(_y_pred_new - _y_true)
        _y_pred_new_original_error = np.linalg.norm(_y_pred_original_new - _y_true)

        target_model.save("resources/head_models/" + target + ".h5")
        print("new "+target +" model created and saved")
        print("dataset: ", inputs[0].shape)
        print("best params: ", best_params)
        print("creating master model ...")
        regenerate_master_model()
        print("new master model created and saved")
        K.clear_session()
        return True

    print("no better model found")
    return False


def regenerate_master_model():
    pre_trained_list = get_available_targets()
    models = {}

    layers = {}
    vggish_input = Input(shape=(5, 128), name='vggish0_input')
    vessel_input = Input(shape=(6,), name='vessel0_input')

    for target in pre_trained_list:
        models[target] = load_model("resources/head_models/" + target + ".h5")
        layers[target] = (models[target])([vggish_input, vessel_input])
        layers[target].trainable = False

    model = Model(inputs=[vggish_input, vessel_input], outputs=list(layers.values()))

    model.save("resources/head_models/master_model.h5")

    return

