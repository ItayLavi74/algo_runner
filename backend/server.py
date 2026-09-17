from flask import Flask, request, jsonify
from dijkstra import dijkstra
from data_validation import isValidData

app = Flask(__name__)

@app.route("/api/receive", methods=["POST"])
def receive():
    data = request.get_json()

    response = isValidData(data)

    if not response["isValid"]:
        return jsonify(response["message"]), 400

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