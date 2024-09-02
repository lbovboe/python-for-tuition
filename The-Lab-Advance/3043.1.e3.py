"""
Learning Objectives:
- Dictionary: create, access and find key existence
- Understanding how to modify dictionary to simplify solution
- If student is stuck, guide in steps
		create dictionary
		accessing
		finding existence
		loop till invalid
"""
######################################################################################
# OPTION 1 ###########################################################################
######################################################################################
# Create dictionary.
# Use a two-way key (all strings) to simplify the solution.
# If student uses the long method (example at the bottom), show him this method

dictionary = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
							'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
							"1": "Jan", "2": "Feb", "3": "Mar", "4": "Apr", "5": "May", "6": "Jun",
							"7": "Jul", "8": "Aug", "9": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

while True:
		# input key
		month = input('Input: ')

		# display result if valid
		if month in dictionary:
				print(dictionary[month])

		# else display invalid and end
		else:
				print('Invalid')
				break

######################################################################################
# OPTION 2 ###########################################################################
######################################################################################
# Students may use the following dictionary and more steps will be needed
dictionary = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
							'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

# get key and value lists
key_list = list(dictionary.keys())
value_list = list(dictionary.values())
# cast values to string for easy comparision
for i in range(12):
		value_list[i] = str(value_list[i])

while True:
		# input key
		month = input('Input: ')

		# display result if valid
		if month in dictionary:
				print(dictionary[month])

		# input exists in value list
		elif month in value_list:
				# search which value and display the key using same index
				# (the keys and values are in the same order)
				for i in range(12):
						if month == value_list[i]:
								print(key_list[i])

		# else display invalid and end
		else:
				print('Invalid')
				break