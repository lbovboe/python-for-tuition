"""
Learning Objectives:
- Learn about string manipulation: extracting substring
- When students are stuck, guide in steps the codes below
"""

#### the following steps can be combined depending on the student's proficiency

# input string
text = input("Input: ")

# split into words
text = text.split()

# the last word is the subject
word = text[2]

# drop "?"
word = word[:-1]

# display word
print(word)