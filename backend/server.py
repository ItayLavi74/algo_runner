from flask import Flask, request, jsonify
from flask_cors import CORS

from data_validation import is_valid_data
from algorithm_documentation import AlgorithmResult
from algorithms_info import *

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])


@app.route("/api/receive", methods=["POST"])
def receive():
    data = request.get_json()
    data_validation, http_error_status_Code = is_valid_data(data)

    if not data_validation["is_valid"]:
        return jsonify(data_validation["messages"]), http_error_status_Code

    algortihm_function = get_algorithm_function(data["algorithm"])

    steps, result = algortihm_function(data)

    return jsonify(AlgorithmResult(algorithm=data["algorithm"],
                                   steps=steps,
                                   result=result)), 200


# learn later
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
