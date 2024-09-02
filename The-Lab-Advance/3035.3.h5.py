"""
Learning Objectives:
- for-loop with string operators * +
- generating multiple running sequences with one loop
"""
# enter integer
num = input("Input number of rows: ")
num = int(num)

# Guide the student to use "." in place of " " to allow visual checking.
# Get the "." sequence correct then add the first "#" sequence, then the second "#" sequence
for i in range(0, num, 1):
		print(" "*(num-i-1) + "#"*(i+1) + "#"*i)