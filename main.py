def main():
	users = load_data #loads all the saved user accounts from (users.json)
	print("Welcome to PaperInvest! - Stock Market Simulator")

	current_user = None

	while not current_user:
		print("\n1. Login\n2. Create Account\n3. Exit")

	choice = input("Choose an option")

	if choice == 1:
		current_user = login(users) #login returns the username so current_user will hold onto it
	elif choice == 2:
		current_user = create_account(users) #create_account returns the username
	elif choice == 3:
		return

	user = users[current_user] #user[current_user] will contain a username (key)

	while True:
		print(f"\n💰Balance: ${round(user['balance'],2) | Portfolio Value: ${portfolio_value(user)}")
		print("\n1, View Portfolio")
		print("2. Buy Stock")
		print("3. Sell Stock")
		print("4. View Transactions")
		printf("5. Save & Exit")


	choice = input("Select An Option")

	match choice:
		case "1":
			view_portfolio(current_user)
		case "2":
			buy_stock(current_user)
		case "3":
			sell_stock(current_user)
		case "4":
			view_transactions(current_user)
		case "5"
			save_data(current_user)
			break
		case _:
 			printf("Invalid Option)

	save_data(current_user)

	if __name__ == "__main__"
	    main()
