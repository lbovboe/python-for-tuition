"""
Learning Objectives:
- Learn about mutating adjacent cells in 2D list.
- When students are stuck, follow the steps in the solution in the order
		main
		display()
		spread()
"""
import copy


# function to display in the format:
# Day N
# X X X X
# X X X X
# X X X X
def display(space, row, col, day):
		print("Day", day)
		for r in range(row):
				for c in range(col):
						print(space[r][c], end=" ")
				print()


# function to spread to neighbour
def spread(space, row, col):

		# Take note of a problem:
		# given 1 0 0 0 0
		# when you use a loop and check there a 1 so you spread to the right
		# then the next iteration, the right had become a 1 so you continue to spread
		#
		# to resolve this problem, one way is to create a copy of space for checking while
		# you update the space so that newly spread cell will not be used for spreading.
		#
		# another way without copying is to set to another value, say 2, instead of 1 and then
		# run a second round of loop to set all the 2 to 1. but will need more if statements
		copySpace = copy.deepcopy(space)

		# loop for each cell
		for r in range(row):
				for c in range(col):

						# if cell is live set it to 1
						if copySpace[r][c] == 1:

								# it does not matter if the neighbours are already a 1
								# just set them to 1

								# check that it has a top neighbour
								if (r - 1) >= 0:
										space[r-1][c] = 1
								# check that it has a bottom neighbour
								if (r + 1) < row:
										space[r+1][c] = 1
								# check that it has a left neighbour
								if (c - 1) >= 0:
										space[r][c-1] = 1
								# check that it has a right neighbour
								if (c + 1) < col:
										space[r][c+1] = 1


# main #######################################

# enter size
size = input("Enter grid size (row column): ")
row, col = size.split()
row = int(row)
col = int(col)

# enter position
position = input("Enter cell position (row column): ")
posRow, posCol = position.split()
posRow = int(posRow)
posCol = int(posCol)

# create space list and set position to 1
space = [[0 for c in range(col)] for r in range(row)]
space[posRow][posCol] = 1

# starts from Day 0
day = 0
display(space, row, col, day)

# loop until all corners are set to 1
while space[0][0] == 0 or space[0][col-1] == 0 or \
				space[row-1][0] == 0 or space[row-1][col-1] == 0:
		day = day + 1
		spread(space, row, col)
		display(space, row, col, day)

# display days
print("Total", day, "days")