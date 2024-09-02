"""
Learning Objectives:
- Learn about Cartesian Coordinates: left-right boundaries from list of points
- When students are stuck, follow the steps in the solution in the order
		main
		boundary()
"""

# function to find min x and max x values from a list of points (left-right boundaries)
def boundary(points):

		# set min and max to first x and iterate through remaining list
		minX = points[0][0]
		maxX = points[0][0]
		for i in range(1, len(points)):

				# store the smaller x
				if minX > points[i][0]:
						minX = points[i][0]

				# store the bigger x
				if maxX < points[i][0]:
						maxX = points[i][0]

		return minX, maxX


# main ##########################################

# loop and append entry of points to list
# and break when "0,0" entered
points = []
while True:
		pt = input("Enter point (x,y): ")

		if pt == "0,0":
				break
		else:
				pt = pt.split(",")
				pt[0] = float(pt[0])
				pt[1] = float(pt[1])
				points.append(pt)

# find boundary and display results
minX, maxX = boundary(points)
print("min x", minX)
print("max x", maxX)