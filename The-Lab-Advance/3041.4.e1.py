"""
Learning Objectives:
- Using floor division operator to find whole number of division
- When students are stuck, guide in steps
		main
		fraction()
"""

def fraction(frac):
		# split and cast
		numerator, denominator = frac.split("/")
		numerator = int(numerator)
		denominator = int(denominator)

		# find whole number and return result
		whole = numerator // denominator
		return whole


# main ######################################
# enter fraction as a string
frac = input("Input a fraction (a/b): ")

# call function and display result
print(fraction(frac))