from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        project="HShops",
        message="Welcome to HShops",
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/version")
def version():
    return jsonify(version="1.0.0")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
