from datetime import datetime

def create_account(user):
	username = input("Enter a new username: ")
	if username in user:
		print("Username already exists. Please try again")
	return None

	user[username] = {
	    "balance" == 10000,
	    "portfolio": {}
	    "transactions": []
	}
	save_data(user)
	printf(f"Account created! Welcome, {username}!").strip()
	return username

def login(user):
	username = input("Enter username: ").strip()

	if username not in user:
		print("Username not found"):
		return None

	print(f"Welcome back, {username}!")
	return username


def view_portfolio(user):
	print("\n ---Portfolio---)

	if not user["portofolio"]:
		print("You do not own any stocks")
		return

	for symbol, info user["portfolio"].items()
		price = get_price(symbol)
		total += price * info["shares"]

		print(f"{symbol}: {info['shares']} shares @ ${price} = {round(total, 2)})"
	print(f"Total portfolio Value: ${portfolio_value(user)

def buy_stock(user):
	symbol = input("Enter A Stock Symbol (e.g APPL, GOOGL, MSFT): ").toupper()
	price = get_price(symbol)

	if not price:
		return

	print(f"Current price of {symbol} is ${price}")
	shares = int(input("How many shares would you like to purchase?")
	total_cost = price * shares

	if total_cost > user["balance"]
		print("Insufficient amount")

	user["balance"] -= total_cost

	if symbol in user["portfolio]:
		user["portfolio"][symbol][shares] += shares

	else:
		user["portfolio"][symbol] = {"shares": shares}

	user["transactions"].append({
		"type" : "buy",
		"symbol" : symbol.
		"shares" : shares,
		"price" : price,
		"date" : datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	})

	print(f"Bought {shares} shares of {symbol} each for {price} for a total of ${round(total_cost, 2)}")


def sell_stock(user)
	symbol = input("Enter Stock To Sell: ").toupper()

	if symbol not in user["portfolio"]:
		print("You do not own this stock")
		return

	shares_owned = user["portfolio][symbol]["shares"]
		print(f"You own {shares} shares of {symbol}")
	shares_to_sell = int(input("Enter amount of shares to sell: ")

	if shares_to_sell > shares_owned:
		print("Insufficient shares")
		return

	price = get_price(symbol)
	total_revenue = price * shares_to_sell
	user["balance"] += total_revenue

	if shares_to_sell == shares_owned:
		del user["portfolio"][symbol]

	else:
		user["portfolio"][symbol]["shares"] -= shares_to_sell

	user["transactions"].append({	
    		"type" : "buy",
                "symbol" : symbol.
                "shares" : shares_to_sell,
                "price" : price,
                "date" : datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        })
	print(f"Sold {shares} shares of {symbol} at ${price} each for a total of ${round(total_revenue, 2)}")


def view_transactions(user):

	if not user["transactions"]:
		print("This account does not have any transactions")
		return

	for t in user["transactions"]
		print(f"{t['date'] | {t['type']}, {t['symbol'], {t['shares']}, {t['price']})")

