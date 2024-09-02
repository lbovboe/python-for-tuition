"""
Learning Objectives:
- Using nested for-loop and controlling the ranges
- Using end=" " to control display format
- Using print() to move to new line
- If students are stuck, guide them to:
		implement the count loop first (y)
		then add on the repeat number of times (x)
		then add the print() to move to new row
"""
# enter numbers and cast to integer
nums = input("Input 2 positive integers: ")
x, y = nums.split()
x = int(x)
y = int(y)

# repeat x number of times
for i in range(x):

		# loop to display count
		for j in range(0, y+1, 1):
				print(j, end=" ")

		# move cursor to next line
		print()