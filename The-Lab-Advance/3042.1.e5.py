"""
Learning Objectives:
- Creating 2D list
- Displaying 2D list
- Adjusting cell values
- When students are stuck, guide in steps
		main
		display()
"""
import random


def display(list2d):

		# Student may use row by row printing method.
		# Below shows cell by cell printing method.
		for r in range(len(list2d)):
				for c in range(len(list2d[r])):
						print(list2d[r][c], end=" ")
				print()


def increase(list2d):

		# Increase each item value by 1
		for r in range(len(list2d)):
				for c in range(len(list2d[r])):
						list2d[r][c] += 1
						# set to 0 if it is 10
						if list2d[r][c] == 10:
								list2d[r][c] = 0


# main ###########################################

# input row and column of 2D list
size = input("Input row size and column size: ")
row, col = size.split()
row = int(row)
col = int(col)

# create 2D list using loop method
list2d = [[random.randint(0, 9) for i in range(col)] for i in range(row)]

# display 2D list
display(list2d)

# call function to increase cell value
increase(list2d)

# display 2D list
print("After increasing by 1")
display(list2d)