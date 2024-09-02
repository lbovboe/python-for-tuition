"""
Learning Objectives:
- Manipulate string via converting it to list
"""
# Enter text
text = input("Input string: ")

# convert to list and display
strings = list(text)

# Use loop to check each character
for i in range(0, len(strings), 1):
		# Student may use different ways to check
		# If his method is lengthy, show him the following (taught in notes under List)
		if strings[i].lower() in ["a", "e", "i", "o", "u"]:
				strings[i] = "."

# If students display the list directly,
# ask them to convert back to single string as the question is to edit a string
# so the original form should be maintained.
text = "".join(strings)
print(text)