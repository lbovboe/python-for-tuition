"""
Learning Objectives:
- Learn about string manipulation: matching & substring
- When students are stuck, guide in steps
		inputting
		detecting exact match
		detecting substring existence
"""

# input words
words = input("Input 2 words: ")
word1, word2 = words.split()

# check exact match
if word1 == word2:
		print("match")

# check substring existence
elif word1 in word2 or word2 in word1:
		print("similar")

# no match
else:
		print("different")