"""
Learning Objectives:
- Learn about Cartesian Coordinates: comparing points in floats
- When students are stuck, follow the steps in the solution in the order
		main
		compare()
"""


# function to compare if 2 points form the following and return the string result:
#   same point
#   horizontal line
#   vertical line
#   slanted line
# they can choose to pass the points as lists or otherwise
def compare(ax, ay, bx, by):

		# students can also use nested if or otherwise for the comparison
		# below method are visually clearer

		# if they have the same x and same y, they are the same point
		if ax == bx and ay == by:
				return "same point"

		# if they have different x but same y, they form a horizontal line
		elif ax != bx and ay == by:
				return "horizontal line"

		# if they have same x but different y, they form a vertical line
		elif ax == bx and ay != by:
				return "vertical line"

		# otherwise they form a slanted line
		else:
				return "slanted line"


# main ###############################################

# enter pointA
point = input("Enter point A (x,y): ")
ax, ay = point.split(",")
ax = float(ax)
ay = float(ay)

# enter pointB
point = input("Enter point B (x,y): ")
bx, by = point.split(",")
bx = float(bx)
by = float(by)

# compare and display result
result = compare(ax, ay, bx, by)
print(result)