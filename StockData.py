# data_handler.py
import yfinance as yf
import matplotlib.pyplot as plt
import json
import os

DATA_FILE = "users.json"

class StockData:
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

    def get_price_change(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period="2d")

            if len(data) < 2:
                return None

            prev_close = data["Close"].iloc[-2]
            current_close = data["Close"].iloc[-1]
            percent_change = ((current_close - prev_close) / prev_close) * 100

            return round(percent_change, 2)
        except Exception:
            print(f"Error fetching data for {symbol}")
            return None

    def display_top_gainers(self):
        stocks = ["GOOGL", "AAPL", "MSFT", "AMZN", "NVDA", "TSLA", "META", "NFLX"]
        changes = []

        for symbol in stocks:
            change = self.get_price_change(symbol)
            if change is not None:
                changes.append((symbol, change))

        top_gainers = sorted(changes, key=lambda x: x[1], reverse=True)[:5]

        print("\n 🗠 [Top 5 Gainers]")
        for symbol, change in top_gainers:
            print(f"[{symbol}]: +{change}%")

    def display_top_losers(self):
        stocks = ["GOOGL", "AAPL", "MSFT", "AMZN", "NVDA", "TSLA", "META", "NFLX"]
        changes = []

        for symbol in stocks:
            change = self.get_price_change(symbol)
            if change is not None:
                changes.append((symbol, change))

        top_losers = sorted(changes, key=lambda x: x[1])[:5]

        print("\n 📉 [Top 5 Losers]")
        for symbol, change in top_losers:
            print(f"[{symbol}]: {change}%")


    def display_price_history(symbol, period, interval):

	try:
		stock = yf.Ticker(symbol)
		data = stock.history(period=period, interval=interval)

		if data.empty:
			print("No data found for this stock)
			return

		plt.figure(figsize=(10,5))
		plt.plot(data.index, data["Close"], label= f"{symbol}, Price", color="blue")
		plt.title(f"{symbol} price history ({period})")
		plt.xlabel("Date")
		plt.ylabel("Price [USD]")
		plt.grid(True)
		plt.legend()
		plt.show()


	except Exception as e:
		print(f"Error fetching data for {symbol}: {e}")
