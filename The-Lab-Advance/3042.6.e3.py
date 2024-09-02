"""
Learning Objectives:
- Learn about Cartesian Coordinates: comparing points in floats
- When students are stuck, follow the steps in the solution in the order
		main
		compare()
"""

# function to compare if 2 points form a vertical line
# they can choose to pass the points as lists or otherwise
def compare(ax, ay, bx, by):

		# if they have same x but different y, they form a vertical line
		if ax == bx and ay != by:
				return True
		else:
				return False


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