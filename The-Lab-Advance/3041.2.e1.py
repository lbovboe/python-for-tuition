"""
Learning Objectives:
- Function: function with parameters and return value
- calling function with variables as parameter and receiving return value
- understanding data type of parameters
- When students are stuck, guide in steps
		multiply()
		main
"""


def multiply(x, y):
		# student may also calculate and return directly
		result = x * y
		return result


# main ########################################

# enter integers
num = input("Input 2 integers: ")
x, y = num.split()
x = int(x)
y = int(y)

# call function and display result
# student may print return value directly
result = multiply(x, y)
print(result)