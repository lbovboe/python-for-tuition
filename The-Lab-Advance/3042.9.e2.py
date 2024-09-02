"""
Learning Objectives:
- Learn about collision detection: intersecting region with top-bottom boundaries
- When students are stuck, follow the steps in the solution in the order
		main
		intersect()
"""


# function to find intersection of point within region bounded by minY and maxY
def intersect(point, minY, maxY):

		# check y within minY to maxY
		if point[1] >= minY and point[1] <= maxY:
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
x = input("Enter min y and max y: ")
minY, maxY = x.split()
minY = int(minY)
maxY = int(maxY)

# check intersection and display result
result = intersect(pt, minY, maxY)
print(result)
