"""
Learning Objectives:
- Creating 2D list
- Displaying 2D list
- Changing a cell value
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


# main ###########################################

# input row and column of 2D list
size = input("Input row size and column size: ")
row, col = size.split()
row = int(row)
col = int(col)

# create 2D list using loop method
list2d = [[0 for i in range(col)] for i in range(row)]

# display 2D list
display(list2d)

# enter row and column of cell and set to 1
cell = input("Input row and column: ")
r, c = cell.split()
r = int(r)
c = int(c)
list2d[r][c] = 1

# display 2D list again
display(list2d)