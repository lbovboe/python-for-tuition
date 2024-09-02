"""
Learning Objectives:
- using end=" " to control display format
"""
# enter number and cast to integer
num = input("Input integer: ")
num = int(num)

# loop to display count
for i in range(0, num+1, 1):
		print(i, end=" ")