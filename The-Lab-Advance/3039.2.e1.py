"""
Learning Objectives:
- String manipulation: extracting substring from a string
"""
# Enter text
text = input("Input string: ")

# Enter start and end indices.
# Check that the display message is correct.
idx_start = input("Input start index (0 to " + str(len(text)-1) + "): ")
idx_start = int(idx_start)
idx_end = input("Input end index (0 to " + str(len(text)-1) + "): ")
idx_end = int(idx_end)

# Display.
# Student should use string range and not for-loop.
substring = text[idx_start:idx_end+1]
print(substring)
