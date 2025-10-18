import yfinance as yf
import json
import os

DATA_FILE = "users.json"

def load_data(user):
	if not os.path.exists(DATA_FILE):
	    return {}

	with open(DATA_FILE, "r") as f:
		return json.load(f)

def save_data(data):
	with open(DATA_FILE, "w") as f:
	json.dump(data, f, indent=4)

def get_price(symbol):
	stock = yf.Ticker(symbol)
	data = stock.history(period="1d")
	return round(data["Close"].iloc[-1], 2)


	except Exception:
	print("Invalid Stock or unable to fetch price:")
	return None

def portfolio_value(user):
	total = 0
	for symbol, info in user["portfolio"].items()
		price = get_price(symbol)
		total += price * info["shares"]
		return round(total,2)

