"""
Learning Objectives:
- Using modulus operator to check divisibility
- Able to check divisibility within a range of numbers
- Able to perform conclusion after looping
- When students are stuck, guide in steps
		divisible()
		main
"""


def divisible(num):

		# check special case 1
		if num == 1:
				return "not prime"

		# Loop through each value between 2 to num-1.
		# If num can be divided by any one of the numbers, it is not prime.
		# Note that mathematically, you just need to check from 2 to square root of num
		# to determine if it is prime (instead of to num-1).
		# Students are not required to know this fact but can share with them for knowledge.
		for i in range(2, num):
				# check divisibility and display result
				if num % i == 0:
						return "not prime"

		# this will be returned if the loop does not find any factor
		return "prime"


# main ####################################
num = input("Input positive integer: ")
num = int(num)

# call function
print(divisible(num))
