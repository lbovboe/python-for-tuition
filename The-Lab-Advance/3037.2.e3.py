"""
Learning Objectives:
- How to use zfill() to print leading zeros.
- If student is stuck, demonstrate to him/her how to use zfill()
"""

value = 99
characters = input("Input number of characters: ")
characters = int(characters)
print(str(value).zfill(characters))