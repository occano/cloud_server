from keras.layers import Input
from keras.optimizers import Adam
import keras.backend as K
from keras.models import Model, load_model
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
            "break_power_mean": 'break_power',
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


    inputs = [np.array(inputs1), np.array(inputs2)]

    target = ui_dict[manual_correction["viewed_field"]]

    corrected = np.full((len(features)), float(manual_correction["manual_corrected_value"]))

    test_set = pickle.load(open("resources/head_models/"+target+"testset.p", "rb"))

    original_testset = test_set

    test_set = list(test_set)

    test_set[0][0] = np.array(test_set[0][0].tolist() + inputs1)
    test_set[0][1] = np.array(test_set[0][1].tolist() +inputs2)
    test_set[1] = np.array(test_set[1].tolist() + corrected.tolist())


    best_params = {
        "min_original":np.inf,
        "min_new":np.inf

    }
    for lr in [0.001, 0.0001,0.00001, 0.000001, 0.0000001, 0.00000001]:
        for epochs in [32,64,128]:
            target_model = load_model("resources/head_models/" + target + ".h5")
            optimizer = Adam(lr)
            for l in range(len(target_model.layers)-4):
                target_model.layers[l].trainable = False


            target_model.compile(optimizer=optimizer, loss="mse", metrics=['mae', 'mape'])

            _y_pred_current = target_model.predict(test_set[0]).flatten()
            _y_pred_current_original = target_model.predict(original_testset[0]).flatten()


            target_model.fit(inputs,corrected, epochs = epochs)

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
                    best_params["min_new"] = _y_pred_new_error
                    best_params["min_original"] = _y_pred_new_original_error


            K.clear_session()




    if "epochs" in best_params:
        target_model = load_model("resources/head_models/" + target + ".h5")
        optimizer = Adam(best_params["lr"])
        for l in range(len(target_model.layers) - 4):
            target_model.layers[l].trainable = False

        target_model.compile(optimizer=optimizer, loss="mse", metrics=['mae', 'mape'])

        _y_pred_current = target_model.predict(test_set[0]).flatten()
        _y_pred_current_original = target_model.predict(original_testset[0]).flatten()

        target_model.fit(inputs, corrected, epochs=best_params["epochs"])

        _y_pred_new = target_model.predict(test_set[0]).flatten()
        _y_pred_original_new = target_model.predict(original_testset[0]).flatten()

        _y_true = test_set[1]

        _y_pred_current_error = np.linalg.norm(_y_pred_current - _y_true)
        _y_pred_current_original_error = np.linalg.norm(_y_pred_current_original - _y_true)

        _y_pred_new_error = np.linalg.norm(_y_pred_new - _y_true)
        _y_pred_new_original_error = np.linalg.norm(_y_pred_original_new - _y_true)

        # TODO save, generate master, return positive
        target_model.save("resources/head_models/" + target + ".h5")
        print ("new "+target +" model created and saved")
        regenerate_master_model()
        print("new master model created and saved")

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
