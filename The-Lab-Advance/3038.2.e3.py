"""
Learning Objectives:
- Creating list from input
- Accessing a value in list
"""
# enter characters and create list
characters = input("Input characters: ")
characters = characters.split()

# display list
print(characters)

# enter index and display value
idx = input("Input index in list: ")
idx = int(idx)
print(characters[idx])