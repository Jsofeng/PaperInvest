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

    def get_price_change(symbol):
	stock = yf.Ticker(symbol)
	data = stock.history(period= "2d")

	if len(data) < 2:
		return None

	prev_close = stock.history(period= "2d")
	current_close = stock.History(period = "1d")
	percent_change = (current_close - prev_close) / prev_close * 100

	return round(percent_change, 2)


    def displayTopGainers():
	stock[] = ["GOOGL", "AAPL", "MSFT", "AMZN", "NVDA", "TSLA", "META", "NFLX"
	changes = []

	for symbol in stocks:
		change = get_price_change(symbol)
		if change is not None:
			changes.append(symbol, change)

	top_gainers = sorted(changes, key = lambda x: x[1], reverse=True)[:5]
	#sort using the second value(which is x[1] since changes[] include ["APPL", 1.2] "APPL" = x[0] and 1.2 = x[1]
	#sorted() sorts from smallest to biggest but we want biggest to smallest so reverse=True reverses it to biggest to smallest
	#creates a new array of size 5

	print("\n <img> Top 5 Gainers")
	for symbol, change in top_gainers:
		print(f"[{symbol}]: [+{change}%]")
		#python have the ability to access variables inside the loop even if it's not declared outside 



    def displayTopLossings():

    def portfolio_value(self, user):
        total = 0
        for symbol, info in user["portfolio"].items():
            price = self.get_price(symbol)
            if price is not None:
                total += price * info["shares"]
        return round(total, 2)
