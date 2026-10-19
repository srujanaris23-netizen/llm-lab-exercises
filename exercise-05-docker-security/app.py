
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Docker Security Exercise",
        "status": "running",
        "hostname": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/security-test")
def security_test():
    return jsonify({
        "user_id": os.getuid() if hasattr(os, "getuid") else None,
        "message": "Container security test endpoint"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
