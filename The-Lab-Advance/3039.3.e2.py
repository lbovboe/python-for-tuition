"""
Learning Objectives:
- Converting string to a list of substrings
- Using join() to convert list to string
"""
# Enter text
text = input("Input string: ")

# convert to list and display
strings = text.split()
print(strings)

# convert to single string
text = "".join(strings)
print(text)