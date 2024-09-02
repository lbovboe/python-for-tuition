"""
Learning Objectives:
- Learn about checking neighbours of a cell in 2D list
- When students are stuck, follow the steps in the solution in the order
		main
		change()
		display()
"""


# function to change left and right neighbours of grid[row][col] to 1
def change(grid, row, col):

		# check index of left neighbour within grid
		if (col-1) >= 0 and (col-1) <= 5:
				grid[row][col-1] = 1

		# check index of right neighbour within grid
		if (col+1) >= 0 and (col+1) <= 5:
				grid[row][col+1] = 1


# display a 2D list
def display(grid):

		for r in range(6):
				print(*grid[r])


# main ####################################################

# create 6x6 2D grid
grid = [[0 for c in range(6)] for r in range(6)]

# enter position and set cell to "*"
position = input("Enter position (row col): ")
row, col = position.split()
row = int(row)
col = int(col)
grid[row][col] = "*"

# change left and right neighbours
change(grid, row, col)

# display
display(grid)