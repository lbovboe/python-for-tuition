"""
Learning Objectives:
- Combining string/list manipulation with built-in functions to perform check
- When students are stuck, guide in steps
		main
		palindrome()
"""


def palindrome(text):

		# convert to list of characters for removing
		text = list(text)

		# loop backwards, otherwise index will be out of range as you pop
		# and go towards the end
		for i in range(len(text)-1, -1, -1):
				# pop if character is not a letter
				if text[i].isalpha() == False:
						text.pop(i)

		# Head tail comparison. Student may also create a reverse string and compare.
		# Check from end to center.
		for i in range(len(text)//2):
				if text[i].upper() != text[len(text)-1-i].upper():
						return False

		# return result
		return True


# main ###############################

# enter text
text = input("Input phrase: ")

# call function and display result
if palindrome(text) == True:
		print("Palindrome")
else:
		print("Not Palindrome")