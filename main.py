from UserData import userData
from StockData import stockData

class PaperInvestApp(userData,stockData):
	def __init__(self):
		super().__init__()
		self.user = self.load_data()
		self.current_user = None

	def run(self):
		print("Welcome to PaperInvest! - Stock Market Simulator")

	while not self.current_user:
		print("\n1. Login\n2. Create Account\n3. Exit")
		choice = input("Choose an option")

	if choice == 1:
		self.current_user = self.login(self.user) #login returns the username so current_user will hold onto it
	elif choice == 2:
		current_user = self.create_account(self.user) #create_account returns the username
	elif choice == 3:
		return

	user = self.users[self.current_user] #user[current_user] will contain a username (key)

	while True:
		print(f"\n💰Balance: ${round(user['balance'],2) | Portfolio Value: ${self.portfolio_value(user)}")
		print("\n1. View Portfolio")
		print("2. Buy Stock")
		print("3. Sell Stock")
		print("4. View Transactions")
		print("5. Save & Exit")


	choice = input("Select An Option")

	match choice:
		case "1":
			self.view_portfolio(user)
		case "2":
			self.buy_stock(user)
		case "3":
			self.sell_stock(user)
		case "4":
			self.view_transactions(user)
		case "5":
			self.save_data(user)
			break
		case _:
 			printf("Invalid Option)

	self.save_data(user)

	if __name__ == "__main__":
	    app = PaperInvestApp()
	    app.run();
