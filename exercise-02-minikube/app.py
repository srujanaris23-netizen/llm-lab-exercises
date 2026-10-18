
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "exercise": "Exercise 2 - Minikube Deployment",
        "status": "running",
        "message": "Flask application is running on Kubernetes!"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15000)
