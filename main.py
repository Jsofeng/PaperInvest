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
