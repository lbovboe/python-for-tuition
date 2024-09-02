"""
Learning Objectives:
- Learn about modifying 2D list within a row width
- When students are stuck, guide in steps:
		1. Create the inputs and generate the mat
		2. Display the mat to see. Make sure this is working properly first.
		3. Using loop, set the indicated row to the second symbol

				@@@@@@@@@       @@@@@@@@@
				@@@@@@@@@       @@@@@@@@@
				@@@@@@@@@       ......... < selected row
				@@@@@@@@@  >>>  @@@@@@@@@
				@@@@@@@@@       @@@@@@@@@
				@@@@@@@@@       @@@@@@@@@
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

# enter col
row_index = input("Input row: ")
row_index = int(row_index)

# change mat and display again
for i in range(col):
		mat[row_index][i] = symbol2
display(mat)