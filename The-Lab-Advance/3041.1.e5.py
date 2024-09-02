"""
Learning Objectives:
- Function: function with 1 parameter and no return
- calling function with variable as parameter
- understanding data type of parameter
- When students are stuck, guide in steps
		main
		increase()
	observe if he will perform casting
"""

def increase(num):
		# student may either cast to int within function or outside it
		num = int(num)
		num = num + 5
		print(num)


# main ###########################

num = input("Input number: ")
increase(num)
