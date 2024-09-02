"""
Learning Objectives:
- Learn about modifying 2D list within a row width
- When students are stuck, guide in steps:
		1. Create the inputs and generate the mat
		2. Display the mat to see. Make sure this is working properly first.
		3. Using nested loop, set the indicated column range to the second symbol

				@@@@@@@@@       @@@@@@@@@
				@@@@@@@@@       @@@@@@@@@
				@@@@@@@@@       @@@@@@@@@
				@@@@@@@@@  >>>  ......... < start row
				@@@@@@@@@       .........
				@@@@@@@@@       ......... < end row
				@@@@@@@@@       @@@@@@@@@

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
def change(mat, symbol, srow, erow):

		# student can choose to pass in the col size as parameters
		# or recalculate it
		col = len(mat[0])

		# the row range is from border to row-border
		for r in range(srow, erow+1):
				# the row range is from border to col-border
				for c in range(col):
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

# enter start and end row
rows = input("Input row start to end: ")
start_row, end_row = rows.split()
start_row = int(start_row)
end_row = int(end_row)

# change mat and display again
change(mat, symbol2, start_row, end_row)
display(mat)