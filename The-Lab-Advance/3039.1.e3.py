"""
Learning Objectives:
- String manipulation: accessing individual character of a string
- Use of len() to determine length of string
"""
# enter text
text = input("Input string: ")

# enter index
# Check that the display message is correct
idx = input("Input index (0 to " + str(len(text)-1) + "): ")
idx = int(idx)

# display
print(text[idx])
