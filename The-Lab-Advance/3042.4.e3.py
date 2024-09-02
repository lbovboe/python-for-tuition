"""
Learning Objectives:
- Learn about checking neighbours of a cell in 2D list
- When students are stuck, follow the steps in the solution in the order
		main
		change()
		display()
"""


# function to change all neighbours of grid[row][col] to 1
def change(grid, row, col):

		# student may hard code with eight if statements to check the neighbours
		# ask student to use nested loop as follow for practice
		# it is not more efficient but just more elegant and trains them to think in loops

		# set all cells (including the "*" to 1)
		# it is easier to set it back later
		for r in range(row-1, row+2):
				for c in range(col-1, col+2):
						# check indices in range of grid
						if r>=0 and r<=5 and c>=0 and c<=5:
								grid[r][c] = 1

		# set [row][col] back to "*"
		grid[row][col] = "*"


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

# change neighbours
change(grid, row, col)

# display
display(grid)