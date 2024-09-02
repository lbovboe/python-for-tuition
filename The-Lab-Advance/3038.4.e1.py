"""
Learning Objectives:
- Appending list
"""
# input qty
num = input("Input integer: ")
num = int(num)

# loop to append text to string list
strings = []
for i in range(num):
		text = input("Input string " + str(i+1) + ": ")
		strings.append(text)

		# display list
		print(strings)