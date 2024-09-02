"""
Learning Objectives:
- string/list manipulation to perform decryption
- understanding how to reverse a process
- When students are stuck, guide in steps
		main
		decrypt()
"""


def decrypt(text):
		# convert to list of characters as we need to modify the characters
		text = list(text)

		# Do step-2 of encryption first
		# shift front character to back
		character = text.pop(0)
		text.append(character)

		# loop for each character
		for i in range(len(text)):
				# convert character to code
				code = ord(text[i])
				# decrease by 2
				code = code - 2
				# convert back to character
				text[i] = chr(code)

		# convert back to string and return result
		text = "".join(text)
		return text


# main #####################################
# enter encrypted message
encrypted = input("Enter encrypted message: ")

# call function to decrypt it and display result
decrypted = decrypt(encrypted)
print(decrypted)