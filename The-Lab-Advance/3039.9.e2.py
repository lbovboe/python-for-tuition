"""
Learning Objectives:
- Character code: converting character to code with ord()
"""
while True:
		# enter character and show code
		char = input("Enter character: ")
		print(ord(char))

		# break if "-" is entered
		if char == "-":
				break