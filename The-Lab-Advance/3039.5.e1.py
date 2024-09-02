"""
Learning Objectives:
- String manipulation: forming string permutations from a string
- If students are stuck, guide them to implement
		1. create a loop to display each character
		2. create an inner loop to display each character again
		3. in the inner loop add the character in the outer loop with the character inner loop
			 if their indices are different (i.e. not the same item)
- Students may also simply mirror the combination done in previous challenge
"""
# Enter text
text = input("Enter string: ")

total = 0
# For each character...
for i in range(0, len(text), 1):

		# ... pair with every other character in the list
		for j in range(0, len(text), 1):
				if i != j:
						print(text[i] + text[j], end=" ")
						total += 1

# display total
print()
print("Total count:", total)