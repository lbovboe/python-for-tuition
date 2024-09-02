"""
Learning Objectives:
- string/list manipulation to shift character
- When students are stuck, guide in steps
		main
		decrypt()
"""


def decrypt(text):

		# use string range to shift first character to the end
		# students may also convert to list and use list manipulation
		text = text[1:] + text[0]

		# return result
		return text


# main #####################################
# enter encrypted message
encrypted = input("Enter encrypted message: ")

# call function to decrypt it and display result
decrypted = decrypt(encrypted)
print(decrypted)