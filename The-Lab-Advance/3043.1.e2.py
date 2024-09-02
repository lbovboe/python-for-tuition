"""
Learning Objectives:
- Dictionary: create, access and find key existence
- If student is stuck, guide in steps
		create dictionary
		accessing
		finding existence
"""

# create dictionary
dictionary = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
							'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

# input key
month = input('Input: ')

# display result
if month in dictionary:
		print(dictionary[month])
else:
		print('Invalid')