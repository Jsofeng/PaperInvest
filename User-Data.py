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
	symbol = input("Enter A Stock Symbol (e.g APPL, GOOGL, MSFT)")
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


