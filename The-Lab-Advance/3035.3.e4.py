"""
Learning Objectives:
- For-loop with string operator *
- If student is stuck, ask him to refer to previous step and modify the print with a running variable.
"""
# enter integer
num = input("Input number of rows: ")
num = int(num)

# It is acceptable if student uses nested loop.
# Student can also use other range e.g. range(1, num+1)
for i in range(num):
		print("#" * (i+1))