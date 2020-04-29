

from flask import Flask ,send_file
from flask import request

from functions import get_plot


app = Flask(__name__)

@app.route('/ping', methods=['POST','GET'])
def ping():
    return 'P0NG',200

@app.route('/plots', methods=['GET'])
def plots():
    if request.method == 'GET':
        try:
            args = request.args.to_dict()
            for key in ["type","fromdate","todate","imo"]:
                if key not in args.keys():
                    return key+" is missing.", 500

            plot = get_plot(args)

            return send_file(plot)
        except Exception as e:
            print(e)
            return "Error, Ask Nir for help", 500


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,threaded=True)

