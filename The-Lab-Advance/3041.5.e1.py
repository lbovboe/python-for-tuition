"""
Learning Objectives:
- Using isalpha()
- When students are stuck, guide in steps
		check()
		main
"""
def check(text):
		# student may return the result directly
		result = text.isalpha()
		return result


# main ###############################

# enter text
text = input("Input string: ")

# call function and display result
# student may print the result directly
result = check(text)
print(result)