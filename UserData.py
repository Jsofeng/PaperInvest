from datetime import datetime
from StockData import stockData

class userData(stockData):


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
        "transactions": []
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

    if not self.user["portfolio"]:
        print("You do not own any stocks.")
        return

    total_value = 0
    for symbol, info in self.user["portfolio"].items():
        price = self.get_price(symbol)
        shares = info["shares"]
        total = price * shares
        total_value += total
        print(f"{symbol}: {shares} shares @ ${price} = ${round(total, 2)}")

    print(f"Total portfolio value: ${round(total_value, 2)}")

def buy_stock(self, user):
    symbol = input("Enter a stock symbol (e.g. AAPL, GOOGL, MSFT): ").upper()
    price = self.get_price(symbol)

    if not price:
        return

    print(f"Current price of {symbol} is ${price}")
    shares = int(input("How many shares would you like to purchase? "))
    total_cost = price * shares

    if total_cost > self.user["balance"]:
        print("Insufficient balance.")
        return

    self.user["balance"] -= total_cost

    if symbol in self.user["portfolio"]:
        self.user["portfolio"][symbol]["shares"] += shares
    else:
        self.user["portfolio"][symbol] = {"shares": shares}

    self.user["transactions"].append({
        "type": "buy",
        "symbol": symbol,
        "shares": shares,
        "price": price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print(f"Bought {shares} shares of {symbol} at ${price} each for a total of ${round(total_cost, 2)}.")

def buy_partial(self, user):
    symbol = input("What stock do you want to buy (partially)?: ").upper()
    price = self.get_price(symbol)

    if not price:
        return

    print(f"Current price of {symbol} is ${price} per share:")

    shares = float(input("How much would you like to purchase?: "))
    total_cost = shares * price

    if self.user["balance"] < total_cost:
        print("Insufficient balance.")
        return

    self.user["balance"] -= total_cost

    if symbol in self.user["portfolio"]:
        # Portfolio is in quotes because it’s a string literal — the actual name of the key inside the dictionary (all the stocks & shares)
        self.user["portfolio"][symbol]["shares"] += shares
        # symbol isn't in quotes because it's a variable storing the stock
        # shares is in quotes because theres it's the name of another key
    else:
        self.user["portfolio"][symbol] = {"shares": shares}

    self.user["transactions"].append({
        "type": "buy",
        "symbol": symbol,
        "shares": shares,
        "price": price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print(f"Bought {shares} of {symbol} at ${price} each for a total of ${round(total_cost, 2)}")


def sell_stock(self, user):
    symbol = input("Enter stock to sell: ").upper()

    if symbol not in self.user["portfolio"]:
        print("You do not own this stock.")
        return

    shares_owned = self.user["portfolio"][symbol]["shares"]
    print(f"You own {shares_owned} shares of {symbol}.")
    shares_to_sell = int(input("Enter amount of shares to sell: "))

    if shares_to_sell > shares_owned:
        print("Insufficient shares.")
        return

    price = self.get_price(symbol)
    total_revenue = price * shares_to_sell
    self.user["balance"] += total_revenue

    if shares_to_sell == shares_owned:
        del self.user["portfolio"][symbol]
    else:
        self.user["portfolio"][symbol]["shares"] -= shares_to_sell

    self.user["transactions"].append({
        "type": "sell",
        "symbol": symbol,
        "shares": shares_to_sell,
        "price": price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print(f"Sold {shares_to_sell} shares of {symbol} at ${price} each for a total of ${round(total_revenue, 2)}.")

def sell_partial(self, user):
    symbol = input("Enter the stock you want to sell: ").upper()

    if symbol not in self.user["portfolio"]:
        print("You do not own this stock")
        return

    shares_owned = self.user["portfolio"][symbol]["shares"]
    print(f"You own {shares_owned} shares of {symbol}")

    partial_sell = float(input("How much do you want to sell (partially): "))

    if partial_sell > shares_owned:
        print("Insufficient shares")
        return

    price = self.get_price(symbol)
    total_revenue = price * partial_sell
    self.user["balance"] += total_revenue

    if partial_sell == shares_owned:
        del self.user["portfolio"][symbol]
    else:
        self.user["portfolio"][symbol]["shares"] -= partial_sell

    self.user["transactions"].append({
        "type": "sell",
        "symbol": symbol,
        "shares": partial_sell,
        "price": price,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def view_transactions(self, user):
    if not self.user["transactions"]:
        print("This account does not have any transactions.")
        return

    for t in self.user["transactions"]:
        print(f"{t['date']} | {t['type']} | {t['symbol']} | {t['shares']} shares @ ${t['price']}")

