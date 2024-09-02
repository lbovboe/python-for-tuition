"""
Learning Objectives:
- using boolean variable
"""
# enter number
num = input("Input positive integer: ")
num = int(num)

# check divisible by 3 and not by 5.
# students can also use nested if.
# student MUST use a variable to store boolean
# and not print result directly
if num % 3 == 0 and num % 5 != 0:
		check = True
else:
		check = False

print(check)