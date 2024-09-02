"""
Learning Objectives:
- Using modulus operator to check divisibility
- When students are stuck, guide in steps
		divisible()
		main
"""


def divisible(num):
		if num % 3 == 0:
				return True
		else:
				return False


# main ####################################
num = input("Input positive integer: ")
num = int(num)

# Display result.
# Student may print return value directly.
result = divisible(num)
print(result)