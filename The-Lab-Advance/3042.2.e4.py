"""
Learning Objectives:
- Learn about modifying 2D list within a column width
- When students are stuck, guide in steps:
		1. Create the inputs and generate the mat
		2. Display the mat to see. Make sure this is working properly first.
		3. Using nested loop, set the indicated column range to the second symbol

				@@@@@@@@@       @@@@....@
				@@@@@@@@@       @@@@....@
				@@@@@@@@@       @@@@....@
				@@@@@@@@@  >>>  @@@@....@
				@@@@@@@@@       @@@@....@
				@@@@@@@@@       @@@@....@
				@@@@@@@@@       @@@@....@
									 col start^  ^col end

"""


# function to display mat
def display(mat):

		# student can choose to pass in the sizes as parameters
		# or recalculate them
		row = len(mat)
		col = len(mat[0])

		# the following uses the notes format to print 2D list
		for r in range(row):
				for c in range(col):
						print(mat[r][c], end="")
				print("")


# function to change the mat
def change(mat, symbol, scol, ecol):

		# student can choose to pass in the row size as parameters
		# or recalculate it
		row = len(mat)

		# the row range is from border to row-border
		for r in range(row):
				# the row range is from border to col-border
				for c in range(scol, ecol+1):
						mat[r][c] = symbol


############
# main #####
############

# enter row, col, symbol1 and symbol2
row, col = input("Input row size and column size: ").split()
row = int(row)
col = int(col)
symbol1, symbol2 = input("Input 2 characters: ").split()

# Create mat filled with symbol1
mat = [[symbol1 for i in range(col)] for j in range(row)]

# display mat
display(mat)

# enter start and end col
ends = input("Input column start to end: ")
start_col, end_col = ends.split()
start_col = int(start_col)
end_col = int(end_col)

# change mat and display again
change(mat, symbol2, start_col, end_col)
display(mat)