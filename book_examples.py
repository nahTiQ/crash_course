'''Class examples from the book so I don't have to keep recreating this shit.
If you found this from github, I have expanded on the examples in the book. This
is not the module you would expect if it was written verbatim. For example, in
the User subclass Admin, I used a dictionary instead of a list because it makes
more since to check if those values are True versus storing a list of user privi-
leges as strings. There are plenty of other modifications as well, and some are 
documented but some are not. Feel free to use this in your code if you don't want
 to recreate the module yourself.

-nahTiQ // klon3d '''


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

class IceCreamStand(Restaurant):
	'''Model an Ice Cream Stand. This is a sub class of Restaurant'''
	def __init__(self, name, cuisine_type):
		super().__init__(name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', "Reese's", "Hunk o' Chunk"]

	def display_flavors(self):
		for flavor in self.flavors:
			print(flavor.title())


class User:
	# list_of_users = []

	def __init__(self,first_name,last_name,username,address=None,password=None):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.address = address
		self.password = password
		self.login_attempts = 0
		self.locked = False
		self.logged_in = False
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

	def login(self, pw):
		if pw == self.password:
			print(f"Welcome, {self.username}")
			self.logged_in = True
		else:
			print(f"That is not the correct password for account {self.username}")

class Admin(User):
	'''Admin class that is a subclass of User. Give this user object special attributes.
	Book wanted to use a list, but I used a dictionary instead. It makes more sense
	to check if these values are true than to iterate through a list of strings.
	PRIVILAGES ARE STORED IN A SEPERATE CLASS!!
	Access with object_name.privilages.method_name()
	'''

	def __init__(self, first_name, last_name, username, address=None, password=None):
		super().__init__(first_name, last_name, username, address, password)
		self.privileges = Privileges(self.username)


class Privileges:
	'''Assign privilages for each user'''
	def __init__(self, username):
		self.username = username
		self.privileges = {
			'can add post' : True,
			'can delete post' : True,
			'can ban user' : True,
			'can create topic' : True,
			'can promote users' : False,
				}

	def show_privileges(self):
		print(f'{self.username} privileges:')
		for privy, t_f in self.privileges.items():
			if self.privileges[privy] == True:
					print(f"\t {privy}")
		
		print(f'{self.username} can NOT:')
		for privy, t_f in self.privileges.items():
			if self.privileges[privy] == False:
				print(f'\t{privy}')

class Car:
	'''Simple attempt at modeling a car'''
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = (f"{self.year} {self.make} {self.model}")
		long_name = long_name.title()
		return long_name

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it")

	def update_odemeter(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the update_odemeter")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery:
	'''Simple model of a battery'''
	def __init__(self, battery_size=75):
		self.battery_size = battery_size

	def describe_battery(self):
		'''Print statement describing the battery size'''
		print(f"This car has a {self.battery_size}-kWh battery")

	def get_range(self):
		'''Print a statement about the range this battery provides.'''
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		'''Check to see if the battery is set to the highest available upgrade'''
		if self.battery_size != 100:
			print(f'Installing upgraded battery to vehicle...')
			self.battery_size = 100
		else:
			"This vehicle already has the maximum battery size!"


class ElectricCar(Car):
	'''Represent aspects of a car, specific to electric vehicles.'''

	def __init__(self, make, model, year):
		'''Initialize attributes of the parent class'''
		super().__init__(make, model, year)
		self.battery = Battery()

	


	
