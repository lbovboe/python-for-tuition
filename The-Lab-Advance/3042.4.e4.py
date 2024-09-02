"""
Learning Objectives:
- Learn about checking neighbours of a cell in 2D list
- When students are stuck, follow the steps in the solution in the order
		main
		change()
		display()
"""


# function to update all bomb neighbours' values
def change(grid):

		# check each cell for bomb
		for row in range(6):
				for col in range(6):

						if grid[row][col] == "*":
								# student may hard code with eight if statements to check the neighbours
								# ask student to use nested loop as follow for practice
								# it is not more efficient but just more elegant and trains them to think in loops

								# check each neighbour add 1 to non-bomb cell
								# since the [row][col] is a bomb, it will not be adjusted
								for r in range(row-1, row+2):
										for c in range(col-1, col+2):
												# check indices in range of grid
												if r>=0 and r<=5 and c>=0 and c<=5:
														# if it is not a bomb, ADD 1 (not set 1)
														if grid[r][c] != "*":
																grid[r][c] += 1

								# display can be added here to see incremental update
								# display(grid)
								# print()


# display a 2D list
def display(grid):

		for r in range(6):
				print(*grid[r])


# main ####################################################

# create 6x6 2D grid
grid = [[0 for c in range(6)] for r in range(6)]

# enter positions and set cells to "*"
numBombs = input("Enter number of bombs: ")
for i in range(int(numBombs)):
		position = input("Enter bomb " + str(i+1) + " position (row col): ")
		row, col = position.split()
		grid[int(row)][int(col)] = "*"

# change left and right neighbours
change(grid)

# display
display(grid)