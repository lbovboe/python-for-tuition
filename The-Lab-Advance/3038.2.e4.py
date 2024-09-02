"""
Learning Objectives:
- Creating list from input
- Checking index within range and accessing a value in list
"""
# enter characters and create list
characters = input("Input characters: ")
characters = characters.split()

# display list
print(characters)

# enter index
idx = input("Input index in list: ")
idx = int(idx)

# check index range and display
if idx < len(characters):
		print(characters[idx])
else:
		print("index out of range")