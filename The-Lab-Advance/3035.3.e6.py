"""
Learning Objectives:
- for-loop with string operators * +
- reversing running sequence
"""
# enter integer
num = input("Input number of rows: ")
num = int(num)

# Guide the student to use "." in place of " " to allow visual checking.
# Get the "." sequence correct then add the "#" sequence
for i in range(0, num, 1):
		print("."*(num-i-1) + "#"*(i+1))