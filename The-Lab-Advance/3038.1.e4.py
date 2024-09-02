"""
Learning Objectives:
- Creating and displaying list indices and values in reverse order
"""
# Students may use any method to create the list
letters = ['A', 'B', 'C', 'D', 'E']

# display list using the methods below.
# Students may use different range.
print(letters)
for i in range(len(letters)-1, -1, -1):
		print(i, letters[i])