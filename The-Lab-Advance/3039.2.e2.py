"""
Learning Objectives:
- String manipulation: extracting substring from a string
- If students are stuck, guide in steps:
		input (take care of display message)
		extracting substring using string range
		loop with break condition
"""
# Enter text
text = input("Input string: ")

while True:
		# Enter start and end indices.
		# Check that the display message is correct.
		indices = input("Input start index and end index (0 to " + str(len(text)-1) + "): ")
		idx_start, idx_end = indices.split()
		idx_start = int(idx_start)
		idx_end = int(idx_end)

		# Display.
		# Student should use string range and not for-loop.
		substring = text[idx_start:idx_end+1]
		print(substring)

		# end if substring <= 2 characters
		if len(substring) <= 2:
				break

