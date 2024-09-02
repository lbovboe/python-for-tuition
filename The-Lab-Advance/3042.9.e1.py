"""
Learning Objectives:
- Learn about collision detection: intersecting region with left-right boundaries
- When students are stuck, follow the steps in the solution in the order
		main
		intersect()
"""


# function to find intersection of point within region bounded by minX and maxX
def intersect(point, minX, maxX):

		# check x within minX to maxX
		if point[0] >= minX and point[0] <= maxX:
				return True
		else:
				return False


# main #####################################################

# enter point
pt = input("Enter point (x,y): ")
pt = pt.split(",")
pt[0] = float(pt[0])
pt[1] = float(pt[1])

# enter boundaries
x = input("Enter min x and max x: ")
minX, maxX = x.split()
minX = int(minX)
maxX = int(maxX)

# check intersection and display result
result = intersect(pt, minX, maxX)
print(result)
