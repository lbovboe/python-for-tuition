"""
Learning Objectives:
- Learn about Cartesian Coordinates: comparing points to check for shapes
- When students are stuck, follow the steps in the solution in the order
		main
		length()
"""


# function to find the length of 2 points of a horizontal line
def length(x1, x2):

		result = x2 - x1
		return result


# main ###############################################

# enter point1
point = input("Enter point 1 (x,y): ")
x1, y1 = point.split(",")
x1 = float(x1)
y1 = float(y1)

# enter point2
point = input("Enter point 2 (x,y): ")
x2, y2 = point.split(",")
x2 = float(x2)
y2 = float(y2)

# enter point3
point = input("Enter point 3 (x,y): ")
x3, y3 = point.split(",")
x3 = float(x3)
y3 = float(y3)

# enter point4
point = input("Enter point 4 (x,y): ")
x4, y4 = point.split(",")
x4 = float(x4)
y4 = float(y4)

# the horizontal length is the length between point1 and point2
# only need to pass in the x values
# the other values are not in use for this step
result = length(x1, x2)
print(result)