from flask import Flask, jsonify
from threading import Lock

app = Flask(__name__)

TOTAL_STOCK = 10
stock = TOTAL_STOCK
stock_lock = Lock()

@app.route("/")
def home():
    return jsonify({
        "exercise": "Exercise 3 - Flash Sale",
        "message": "Flash sale application is running",
        "available_stock": stock
    })

@app.route("/buy", methods=["POST"])
def buy():
    global stock
    with stock_lock:
        if stock > 0:
            stock -= 1
            return jsonify({
                "message": "Purchase successful",
                "available_stock": stock
            }), 200
        return jsonify({"message": "Sold out", "available_stock": 0}), 409

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15000)
