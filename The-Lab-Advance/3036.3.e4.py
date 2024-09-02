"""
Learning Objectives:
- Using nested for-loop and controlling the ranges
- Using end=" " to control display format
- Using print() to move to new line
- If students are stuck, guide them to:
		1. implement the inner count loop with range(1, num+1, 1)
		2. add on the repeat number of times
		3. add the print() to move to new row
		4. adjust the start of the range in the inner loop to range(1, num+1-i, 1)
"""
# enter number and cast to integer
num = input("Input positive integer: ")
num = int(num)

# repeat x number of times
for i in range(0, num, 1):

		# loop to display count
		for j in range(1, num+1-i, 1):
				print(j, end=" ")

		# move cursor to next line
		print()