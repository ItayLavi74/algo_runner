from flask import Flask, request, jsonify
from algorithms.dijkstra import dijkstra
from data_validation import is_valid_data

app = Flask(__name__)


@app.route("/api/receive", methods=["POST"])
def receive():
    data = request.get_json()

    data_validation = is_valid_data(data)

    if not data_validation["is_valid"]:
        return jsonify(data_validation["messages"]), 400

    print("data:")
    print(data)

    distences, previous = dijkstra(data["graph"], data["startNode"])
    return jsonify(distences, previous), 200


# learn later
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)
