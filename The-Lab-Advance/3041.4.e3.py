"""
Learning Objectives:
- Using floor division operator to find whole number of division
- Using modulus operator to find proper fraction
- Using loop to simplify fraction
- Formatting result based on answers
- When students are stuck, guide in steps
		main
		fraction()
"""

def fraction(frac):
		# split and cast
		numerator, denominator = frac.split("/")
		numerator = int(numerator)
		denominator = int(denominator)

		# find whole number
		whole = numerator // denominator

		# update numerator to convert to simple fraction
		numerator = numerator % denominator

		# Simplify fraction.
		# Run a loop from numerator to 2
		# to find the biggest number that both numerator and denominator
		# can be divided by
		for i in range(numerator, 1, -1):
				# if both numerator and denominator divisible by i, then divide them to simplify
				if numerator % i == 0 and denominator % i == 0:
						numerator = numerator // i
						denominator = denominator // i
						break

		# return result
		result = str(whole) + " " + str(numerator) + "/" + str(denominator)
		return result


# main ######################################
# enter fraction as a string
frac = input("Input a fraction (a/b): ")

# call function and display result
print(fraction(frac))