"""
Learning Objectives:
- String manipulation: forming string combinations from a string
- If students are stuck, guide them to implement
		1. create a loop to display each character
		2. create an inner loop to display each character again
		3. in the inner loop add the character in the outer loop with the character inner loop
"""
# Enter text
text = input("Enter string: ")

# For each character...
for i in range(0, len(text), 1):

		# ... pair with every character in string
		for j in range(0, len(text), 1):
				print(text[i] + text[j], end=" ")