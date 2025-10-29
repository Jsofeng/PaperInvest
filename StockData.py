# data_handler.py
import yfinance as yf
import json
import os

DATA_FILE = "users.json"

class stockData:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file

    def load_data(self):
        if not os.path.exists(self.data_file):
            return {}

        with open(self.data_file, "r") as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def get_price(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period="1d")
            return round(data["Close"].iloc[-1], 2)
        except Exception:
            print("Invalid stock or unable to fetch price.")
            return None

    def displayTopGainers():

    def displayTopLossings():

    def portfolio_value(self, user):
        total = 0
        for symbol, info in user["portfolio"].items():
            price = self.get_price(symbol)
            if price is not None:
                total += price * info["shares"]
        return round(total, 2)
