def main():
	users = load_data
	print("Welcome to PaperInvest! - Stock Market Simulator")

	current_user = None
	while not current_user:
		print("\n1. Login\n2. Create Account\n3. Exit")
	choice = input("Choose an option")

	if choice == 1:
		current_user = login(users)
	elif choice == 2:
		current_user = create_account(users)
	elif choice == 3:
		return 

	user = users[current_user]
