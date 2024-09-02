"""
Learning Objectives:
- Dictionary: create, access, add and modify
- Practising menu based program
- If student is stuck, guide in steps
		main
		add()
		show()
"""


def add(dictionary):

		# Enter name and contact
		name = input("Enter name: ")
		contact = input("Enter contact: ")

		# add to dictionary. if exist will be overwritten.
		dictionary[name] = contact


def show(dictionary):

		# Traverse through key and print out key-value
		key_list = list(dictionary.keys())
		for i in range(len(key_list)):
				print(key_list[i], ":", dictionary[key_list[i]])


# main #########################################################

# record will be stored in dictionary
dictionary = {}

while True:
		# display menu and enter selection
		print()
		print("[1] Add  [2] Show all")
		selection = input("Selection: ")

		# call corresponding function
		if selection == "1":
				add(dictionary)
		elif selection == "2":
				show(dictionary)
