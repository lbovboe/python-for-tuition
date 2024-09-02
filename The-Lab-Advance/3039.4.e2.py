"""
Learning Objectives:
- String manipulation: forming string combinations from a string
- If students are stuck, guide them to implement
		1. create a loop to display each character
		2. create an inner loop to display each character again
		3. in the inner loop add the character in the outer loop with the character inner loop
		4. remove repetition by modifying start range of inner loop
"""
# Enter text
text = input("Enter names: ").split()

total = 0
# For each character...
for i in range(0, len(text), 1):

		# ... pair with every subsequent character down the list
		for j in range(i+1, len(text), 1):
				print(text[i], text[j])
				total += 1

# display total
print("Total count:", total)