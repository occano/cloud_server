import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import logging
import time
from flask import Flask
from werkzeug.serving import run_simple
from flask import request, jsonify

from functions import correct_target

# set to True to inform that the app needs to be re-created
to_reload = False


logging.basicConfig(filename="server.log",
                    filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)
def get_app():
    app = Flask(__name__)

    @app.route('/reload', methods=['GET'])
    def reload():
        if request.method == 'GET':
            global to_reload
            to_reload = True
            return "reloaded"

    @app.route('/ping', methods=['GET'])
    def ping():
        if request.method == 'GET':
            return "P0NG", 200

    @app.route('/', methods=['GET'])
    def index():
        if request.method == 'GET':
            return "OCCANO", 200

    @app.route('/train', methods=['POST'])
    def _train():

        if request.method in ['POST']:
            try:
                start_time = time.time()
                manual_correction =  request.json["manual_correction"]
                features = request.json['features']
                predictions = request.json['predictions']
                if len(predictions) > 0 :
                    if "additional_features" in predictions[-1].keys():
                        updated = correct_target(features,predictions, manual_correction)

                        response = jsonify({"updated":updated})
                        response.headers.add('Access-Control-Allow-Origin', '*')

                        print("training time performance: ", time.time() - start_time, " sec")

                        return response, 200


                return "no additional features found", 202

            except Exception as e:
                logging.error(str(e))
                print(str(e))
                return str(e), 202

    print("server is up!")
    return app


class AppReloader(object):
    def __init__(self, create_app):
        self.create_app = create_app
        self.app = create_app()

    def get_application(self):
        global to_reload
        if to_reload:
            self.app = self.create_app()
            to_reload = False

        return self.app

    def __call__(self, environ, start_response):
        app = self.get_application()
        return app(environ, start_response)


# This application object can be used in any WSGI server
# for example in gunicorn, you can run "gunicorn app"
application = AppReloader(get_app)

if __name__ == '__main__':
    run_simple('0.0.0.0', 5003, application)
