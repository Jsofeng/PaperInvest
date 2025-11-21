from datetime import datetime
from StockData import StockData

class userData(StockData):

    def __init__(self):  # self is basically "this." in java
        super().__init__()
        self.user = self.load_data()  # .user is initialized to load_data so you dont need to call load_data everytime instead js do .user

    def create_account(self, user):
        username = input("Enter a new username: ").strip()
        if username in self.user:
            print("Username already exists. Please try again.")
            return None

        self.user[username] = {
            "balance": 10000,
            "portfolio": {},
            "transactions": [],
            "history": []
        }
        self.save_data(self.user)
        print(f"Account created! Welcome, {username}!")
        return username

    def login(self, user):
        username = input("Enter username: ").strip()

        if username not in self.user:
            print("Username not found.")
            return None

        print(f"Welcome back, {username}!")
        return username

    def view_portfolio(self, user):
        print("\n--- Portfolio ---")

        if not user["portfolio"]:
            print("You do not own any stocks.")
            return

        total_value = 0
        for symbol, info in user["portfolio"].items():
            price = self.get_price(symbol)
            shares = info["shares"]
            total = price * shares
            total_value += total
            print(f"{symbol}: {shares} shares @ ${price} = ${round(total, 2)}")

        print(f"Total portfolio value: ${round(total_value, 2)}")

    def buy_stock(self, user):
        symbol = input("Enter a stock symbol (e.g. AAPL, GOOGL, MSFT): ").upper()
        self.display_stock_history(symbol, "3mo", "1d")
        price = self.get_price(symbol)

        if not price:
            return

        print(f"Current price of {symbol} is ${price}")
        shares = int(input("How many shares would you like to purchase? "))
        total_cost = price * shares

        if total_cost > user["balance"]:
            print("Insufficient balance.")
            return

        user["balance"] -= total_cost

        if symbol in user["portfolio"]:
            user["portfolio"][symbol]["shares"] += shares
        else:
            user["portfolio"][symbol] = {"shares": shares}

        user["transactions"].append({
            "type": "buy",
            "symbol": symbol,
            "shares": shares,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        print(f"Bought {shares} shares of {symbol} at ${price} each for a total of ${round(total_cost, 2)}.")

    def buy_partial(self, user):
        symbol = input("What stock do you want to buy (partially)?: ").upper()
        self.display_stock_history(symbol, "3mo", "1d")
        price = self.get_price(symbol)

        if not price:
            return

        print(f"Current price of {symbol} is ${price} per share:")

        shares = float(input("How much would you like to purchase?: "))
        total_cost = shares * price

        if user["balance"] < total_cost:
            print("Insufficient balance.")
            return

        user["balance"] -= total_cost

        if symbol in user["portfolio"]:
            user["portfolio"][symbol]["shares"] += shares
        else:
            user["portfolio"][symbol] = {"shares": shares}

        user["transactions"].append({
            "type": "buy",
            "symbol": symbol,
            "shares": shares,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        print(f"Bought {shares} of {symbol} at ${price} each for a total of ${round(total_cost, 2)}")

    def sell_stock(self, user):
        symbol = input("Enter stock to sell: ").upper()
        self.display_stock_history(symbol, "3mo", "1d")

        if symbol not in user["portfolio"]:
            print("You do not own this stock.")
            return

        shares_owned = user["portfolio"][symbol]["shares"]
        print(f"You own {shares_owned} shares of {symbol}.")
        shares_to_sell = int(input("Enter amount of shares to sell: "))

        if shares_to_sell > shares_owned:
            print("Insufficient shares.")
            return

        price = self.get_price(symbol)
        total_revenue = price * shares_to_sell
        user["balance"] += total_revenue

        if shares_to_sell == shares_owned:
            del user["portfolio"][symbol]
        else:
            user["portfolio"][symbol]["shares"] -= shares_to_sell

        user["transactions"].append({
            "type": "sell",
            "symbol": symbol,
            "shares": shares_to_sell,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        print(f"Sold {shares_to_sell} shares of {symbol} at ${price} each for a total of ${round(total_revenue, 2)}.")

    def sell_partial(self, user):
        symbol = input("Enter the stock you want to sell: ").upper()
        self.display_stock_history(symbol, "3mo", "1d")

        if symbol not in user["portfolio"]:
            print("You do not own this stock")
            return

        shares_owned = user["portfolio"][symbol]["shares"]
        print(f"You own {shares_owned} shares of {symbol}")

        partial_sell = float(input("How much do you want to sell (partially): "))

        if partial_sell > shares_owned:
            print("Insufficient shares")
            return

        price = self.get_price(symbol)
        total_revenue = price * partial_sell
        user["balance"] += total_revenue

        if partial_sell == shares_owned:
            del user["portfolio"][symbol]
        else:
            user["portfolio"][symbol]["shares"] -= partial_sell

        user["transactions"].append({
            "type": "sell",
            "symbol": symbol,
            "shares": partial_sell,
            "price": price,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def view_transactions(self, user):
        if not user["transactions"]:
            print("This account does not have any transactions.")
            return

        for t in user["transactions"]:
            print(f"{t['date']} | {t['type']} | {t['symbol']} | {t['shares']} shares @ ${t['price']}")

    def total_account_value(self, user):
        total = user["balance"]
        for symbol, info in user["portfolio"].items():
            # info holds the value of user["portfolio"][symbol]
            price = self.get_price(symbol)
            if price:
                total += price * info["shares"]
        return round(total, 2)

    def record_daily_value(self, user):
        today = datetime.now().strftime("%Y:%m:%d")
        value = self.total_account_value(user)

        if "history" not in user:
            user["history"] = []

        if user["history"] and user["history"][-1]["date"] == today:  # checks if theres already a history and if the most recent entry was today
            user["history"][-1]["value"] = value
            # replace the previous total_account_value with today's
        else:  # if theres no history of the total_account_value
            user["history"].append({"date": today, "value": value})

    def show_daily_gain_loss(self, user):
        if "history" not in user or len(user["history"]) < 2:
            print("Not enough data to show daily gain/loss")
            return

        today = user["history"][-1]["value"]
        yesterday = user["history"][-2]["value"]

        change = today - yesterday
        percent = (change / yesterday) * 100

        print("\n📊 Daily Performance:")
        print(f"Yesterday: ${yesterday}")
        print(f"Today:     ${today}")

        if change >= 0:
            print(f" Gain: +${round(change, 2)} (+{round(percent, 2)}%)")
        else:
            print(f" Loss: -${round(change, 2)} (-{round(percent, 2)}%)")
