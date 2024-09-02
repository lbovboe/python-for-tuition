"""
Learning Objectives:
- Using isalpha(), uppercase()
- String-List conversions and manipulation
- When students are stuck, guide in steps
		convert()
		main
"""
def convert(text):

		# convert to list of characters for removing
		text = list(text)

		# loop backwards, otherwise index will be out of range as you pop
		# and go towards the end
		for i in range(len(text)-1, -1, -1):
				# pop if character is not a letter
				if text[i].isalpha() == False:
						text.pop(i)

		# join back to string and convert to uppercase
		text = "".join(text)
		text = text.upper()

		# return result
		return text


# main ###############################

# enter text
text = input("Input string: ")

# call function and display result
# student may print the result directly
result = convert(text)
print(result)