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


 
