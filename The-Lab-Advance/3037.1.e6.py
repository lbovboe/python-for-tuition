"""
Learning Objectives:
- while True loop with break condition and counter
"""
# students may also use while with condition (variable will need to be initialised)
count = 0
while True:
		name = input("Input name: ")
		if name == "end":
				print(count)
				break
		else:
				count += 1
