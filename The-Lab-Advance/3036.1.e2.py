"""
Learning Objectives:
- the step is leading towards the use of boolean in the subsequent steps
"""
# enter number
num = input("Input positive integer: ")
num = int(num)

# check divisible by 3 and not by 5.
# students can also use nested if
if num % 3 == 0 and num % 5 != 0:
		print(num)