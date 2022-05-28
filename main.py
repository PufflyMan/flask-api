from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/<string:name>")
def api(name: str):
    return jsonify(data=name), 200


if __name__ == "__main__":
    app.run()
