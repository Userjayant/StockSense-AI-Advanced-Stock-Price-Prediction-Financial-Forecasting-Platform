"""Flask web dashboard for Stock Price Prediction."""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from flask import Flask, render_template, request, jsonify
from predict import forecast

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json(force=True)
    ticker = data.get("ticker", "AAPL").strip().upper()
    days = int(data.get("days", 7))
    model = data.get("model", "random_forest")
    try:
        result = forecast(ticker, days=days, model_name=model)
        hist = result["history"]
        date_col = "Date" if "Date" in hist.columns else hist.columns[0]
        return jsonify({
            "ok": True,
            "ticker": result["ticker"],
            "model": result["model"],
            "metrics": result["metrics"],
            "last_close": result["last_close"],
            "history_dates": [str(d)[:10] for d in hist[date_col].tolist()],
            "history_prices": [round(float(p), 2) for p in hist["Close"].tolist()],
            "forecast_dates": result["forecast_dates"],
            "forecast_prices": result["forecast_prices"],
        })
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
