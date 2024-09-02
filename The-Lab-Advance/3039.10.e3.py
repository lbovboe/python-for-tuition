"""
Learning Objectives:
- Learn about string manipulation with list: matching & substring
- When students are stuck, guide in steps
		inputting and saving records
		detecting exact match
		detecting substring existence
"""

# record is a list that stores each input as a string
record = []

# loop to enter a list of words until "end" is entered
while True:

		# enter input
		text = input("Input word: ")
		if text == "end":
				break

		# append to record list
		record.append(text)

# loop to enter a list of words until "end" is entered
while True:

		# enter search string
		search = input("Input search: ")
		if search == "end":
				break

		# iterate through record to find if search string exists
		found = False
		for i in range(len(record)):

				# check for exact match
				if search == record[i]:
						found = True
						print("match")
						break

		# if exact match not found, check substring existence
		if not found:
				for i in range(len(record)):

						# check if search exists as a substring in record
						if search in record[i]:
								found = True
								print("similar to", record[i])
								break

		# no exact match nor substring existence
		if not found:
				print("not found")