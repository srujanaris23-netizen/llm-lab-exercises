from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

def check_host(host, port):
    try:
        with socket.create_connection((host, port), timeout=2):
            return "reachable"
    except OSError:
        return "unreachable"

@app.route("/")
def home():
    return jsonify({
        "exercise": "Exercise 4 - Docker Networking",
        "message": "Flask application is running"
    })

@app.route("/about")
def about():
    return jsonify({
        "application": "Flask",
        "mysql": check_host(MYSQL_HOST, 3306),
        "redis": check_host(REDIS_HOST, 6379)
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
