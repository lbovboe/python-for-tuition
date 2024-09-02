"""
Learning Objectives:
- Using string/list to check mirroring
- When students are stuck, guide in steps
		palindrome()
		main
"""
def palindrome(text):

		# Students may use string or list to compare.
		# Students may use head-tail comparison or
		# create a reverse string to compare

		# head tail comparison.
		# Check from end to center.
		for i in range(len(text)//2):
				if text[i].upper() != text[len(text)-1-i].upper():
						return False

		return True


# main ###############################

# enter text
text = input("Input word: ")

# call function and display result
print(palindrome(text))