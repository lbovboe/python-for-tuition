"""
Learning Objectives:
- String manipulation: accessing individual character of a string via loop
- Use of len() to determine length of string
"""
# enter text
text = input("Input string: ")

# display
for i in range(len(text)):
		print(text[i])
print(len(text))
