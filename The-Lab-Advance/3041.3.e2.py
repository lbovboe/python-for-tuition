"""
Learning Objectives:
- Using modulus operator to check divisibility
- Able to use loop to check divisibility of all numbers in within an integer
	as this is needed for finding prime number
- When students are stuck, guide in steps
		divisible()
		main
"""


def divisible(num):
		# loop through each value 1 to num
		for i in range(1, num+1):
				# check divisibility and display result
				if num % i == 0:
						print(num, "is divisible by", i)
				else:
						print(num, "is not divisible by", i)


# main ####################################
num = input("Input positive integer: ")
num = int(num)

# call function
divisible(num)
