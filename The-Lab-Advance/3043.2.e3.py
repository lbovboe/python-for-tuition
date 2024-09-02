"""
Learning Objectives:
- Dictionary: create, access, add, modify and delete
- Practising menu based program
- If student is stuck, guide in steps
		main
		add()     <-- same as previous step
		show()    <-- same as previous step
		delete()  <-- same as previous step
		search()
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


def delete(dictionary):

		# Enter name
		name = input("Enter name: ")

		# delete if found
		if name in dictionary:
				dictionary.pop(name)
				print("Contact deleted")

		# else display message
		else:
				print("Contact not found")


def search(dictionary):

		# enter search string
		search_str = input("Enter search: ")

		# extract key and value lists
		key_list = list(dictionary.keys())
		value_list = list(dictionary.values())

		# search through each record
		found = False
		for i in range(len(dictionary)):
				# is search_str is a substring of any name or contact, display the record
				# note that it is case insensitive
				if search_str.lower() in key_list[i].lower() or search_str.lower() in value_list[i].lower():
						print(key_list[i], ":", value_list[i])
						found = True

		if found == False:
				print("Contact not found")


# main #########################################################

# record will be stored in dictionary
dictionary = {}

while True:
		# display menu and enter selection
		print()
		print("[1] Add  [2] Delete  [3] Search  [4] Show all")
		selection = input("Selection: ")

		# call corresponding function
		if selection == "1":
				add(dictionary)
		elif selection == "2":
				delete(dictionary)
		elif selection == "3":
				search(dictionary)
		elif selection == "4":
				show(dictionary)
