from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin&vs_currencies=usd"
    "&include_24hr_change=true"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/price")
def price():
    try:
        response = requests.get(COINGECKO_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        return jsonify({
            "price": data["bitcoin"]["usd"],
            "change_24h": round(data["bitcoin"]["usd_24h_change"], 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run()