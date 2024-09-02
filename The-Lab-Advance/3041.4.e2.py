"""
Learning Objectives:
- Using floor division operator to find whole number of division
- Using modulus operator to find proper fraction
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

		# return result
		result = str(whole) + " " + str(numerator) + "/" + str(denominator)
		return result


# main ######################################
# enter fraction as a string
frac = input("Input a fraction (a/b): ")

# call function and display result
print(fraction(frac))