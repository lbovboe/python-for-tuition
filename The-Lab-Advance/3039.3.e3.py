"""
Learning Objectives:
- Manipulate string via converting it to list
"""
# Enter text
text = input("Input string: ")

# Enter index to remove
idx = input("Remove index (0 to " + str(len(text)-1) + "): ")
idx = int(idx)

# convert to list and display
strings = list(text)
strings.pop(idx)

# If students display the list directly,
# ask them to convert back to single string as the question is to edit a string
# so the original form should be maintained.
text = "".join(strings)
print(text)