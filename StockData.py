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
        #x : x[1] means use the second value in the hashmap which is the %
        #key = parameter tells python what value to sort lambda x: x[1] creates a tiny function that returns the second value of each element in the hashmap
        print("\n 📉 [Top 5 Losers]")
        for symbol, change in top_losers:
            print(f"[{symbol}]: {change}%")

    def display_stock_history(self, symbol, period, interval):

        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period=period, interval=interval)

            if data.empty:
                print("No data found for this stock")
                return

            plt.figure(figsize=(10, 5))
            plt.plot(data.index, data["Close"], label=f"{symbol}, Price", color="blue")
            plt.title(f"{symbol} price history ({period})")
            plt.xlabel("Date")
            plt.ylabel("Price [USD]")
            plt.grid(True)
            plt.legend()
            plt.show()

        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")

    def get_announcements(symbol):
        ticker = yf.Ticker(symbol)
        news_items = ticker.news if hasattr(ticker, "news") else []

        announcements = []

        for item in news_items[:5]:
            title = item.get("title", "")
            publisher = item.get("publisher", "")
            announcements.append(f"{title} ({publisher})")


        if not announcements:
            announcements = [f"No recent announcements regarding {symbol.upper()}"]

        return announcements
    
    def get_event_dates(symbol):
        ticker = yf.Ticker(symbol)

        try:
            earnings_df = ticker.get_earnings_dates().reset_index()
            earnings_list = earnings_df.to_dict(orient="records")
        except:
            earnings_list = []

        try:
            dividends = ticker.dividends
            last_dividend_date = dividends.index[-1].strftime("%Y-%m-%d") if len(dividends) > 0 else None
        except:
            last_dividend_date = None

        return {
            "earnings_call": earnings_list[0]["Earnings Dates"].strftime("%Y-%m-%d") if earnings_list else None,
            "dividend_date": last_dividend_date,
            "product_event": None,
        }  