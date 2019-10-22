'''Class examples from the book so I don't have to keep recreating this shit'''

class Restaurant:

	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.customers_served = 0

	def set_number_served(self, number_served):
		self.customers_served = number_served
		print(f"The number of served customers has been manually set to: {self.customers_served}")

	def update_customers(self, increment):
		'''update the amount of customers served by increment'''
		self.customers_served += increment
		print(f"{increment} more customers have been served. The new total of customers served is {self.customers_served}.")

class User:
	list_of_users = []

	def __init__(self,first_name,last_name, username,address,password=None):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.address = address
		self.password = password
		self.login_attempts = 0
		self.locked = False
		'''Add new user object to list of users.
		Figure this shit out later, but probably a scope issue
		User.list_of_users.append(self.username)
		'''	
	def check_login_attempts(self):
		'''Checked to see if a user is locked out and print log-in attempts'''
		print(f"This user has attempted to log in {self.login_attempts} times")
		if self.login_attempts >= 5:
			self.locked = True
			print(f"{self.username} is locked out for log-in attempts.")
		else:
			print(f"{self.username} is not currently locked out.")
		
	def print_user_list(self, list_of_users):
		'''prints a list of all current users'''
		for user in list_of_users:
			print(user)

	def update_log_in_attempts(self, number):
		'''Directly set a login attempt number'''
		self.login_attempts = number

	def reset_log_ins(self):
		self.login_attempts = 0
		if self.login_attempts == 0:
			print(f"The log-ins for {self.username} has been reset.")