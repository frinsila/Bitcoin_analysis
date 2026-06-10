from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

BINANCE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/price")
def price():
    data = requests.get(BINANCE_URL).json()
    return jsonify({"price": float(data["price"])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)