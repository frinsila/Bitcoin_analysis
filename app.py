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
    try:
        response = requests.get(
            "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
            timeout=10
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

        data = response.json()

        return jsonify({
            "price": float(data.get("price", 0))
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)