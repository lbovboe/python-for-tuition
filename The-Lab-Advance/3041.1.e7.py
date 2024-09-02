"""
Learning Objectives:
- Function: function with multiple parameters and no return
- calling function with values as parameters
- understanding data type of parameters
- When students are stuck, guide in steps
		add()
		main
"""


def add(x, y):
		print(x + y)


# main ###########################
x = input("Input integer 1: ")
y = input("Input integer 2: ")

# student can cast to int inside or outside add()
x = int(x)
y = int(y)
add(x, y)
