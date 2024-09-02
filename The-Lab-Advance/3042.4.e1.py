"""
Learning Objectives:
- Learn about checking neighbours of a cell in 2D list
- When students are stuck, follow the steps in the solution in the order
		main
		display()
		count()
"""


import random


# display a 2D list
def display(grid):

		for r in range(3):
				print(*grid[r])


# function to count the border "** and set the value at the centre
def count(grid):

		# set centre to zero first so that it will not be added to count if it is "*"
		grid[1][1] = 0

		# loop through to count.
		# student should not hardcode with eight if statements
		count = 0
		for r in range(3):
				for c in range(3):
						if grid[r][c] == "*":
								count += 1
		grid[1][1] = count


# main ####################################################

# Create a 2D grid
#
# this method uses initialising first but
# is less efficient as it iterates twice:
#     grid = [[0 for c in range(3)] for r in range(3)]
#     for r in range(3):
#         for c in range(3):
#             if random.randint(0, 1) == 1:
#                 grid[r][c] = "*"
#
# the method below uses the appending taught in the notes
grid = []
for r in range(3):
		row = []
		for c in range(3):
				if random.randint(0, 1) == 0:
						row.append(0)
				else:
						row.append("*")
		grid.append(row)

# display the grid
display(grid)

# count the border "*" and update the centre cell with the result
count(grid)
print()
display(grid)