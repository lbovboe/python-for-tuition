"""
Learning Objectives:
- Creating list from input
- Finding length of a list
- Finding last index of a list
"""
# enter characters
characters = input("Input characters: ")

# use split to create as list
characters = characters.split()

# display list
print(characters)

# display length and index range
# Student may display directly e.g. print(len(characters))
length = len(characters)
print(length)
print("0 to", length-1)