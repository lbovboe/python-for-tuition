"""
Learning Objectives:
- Try-exception : error caused by casting
- When students are stuck, guide in steps
		creating the try exception for length
		creating the try exception for breadth
		if student attempt to nest the breadth loop within the length,
		let them do so to see if they face problem ending the program.
"""
# Loop to input length.
while True:
		try:
				# input and cast
				length = input("Input length of rectangle: ")
				length = float(length)

				# check that length is positive
				if length > 0:
						break
				else:
						print("invalid length")
		except:
				print("invalid length")

# Loop to input breadth.
# Student may attempt to nest this loop in the above
# but they may have problem trying to end the program as break only
# exits the nearest loop unless they use additional flag.
# Avoid using quit() or exit() to terminate the program.
while True:
		try:
				# input and cast
				breadth = input("Input breadth of rectangle: ")
				breadth = float(breadth)

				# check that breadth is positive
				if breadth > 0:
						# calculate area and display
						area = length * breadth
						area = round(area, 1)
						print("Area of rectangle is", area)
						break
				else:
						print("invalid breadth")
		except:
				print("invalid breadth")
