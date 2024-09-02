"""
Learning Objectives:
- Character code: accessing every character in a string and convert it to code with ord()
"""
# enter string
text = input("Enter string: ")
for i in range(0, len(text), 1):
		print(ord(text[i]))