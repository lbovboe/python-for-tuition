"""
Learning Objectives:
- Learn about Cartesian Coordinates: top-bottom boundaries from list of points
- When students are stuck, follow the steps in the solution in the order
		main
		boundary()
"""

# function to find min y and max y values from a list of points (top-bottom boundaries)
def boundary(points):

		# set min and max to first y and iterate through remaining list
		minY = points[0][1]
		maxY = points[0][1]
		for i in range(1, len(points)):

				# store the smaller y
				if minY > points[i][1]:
						minY = points[i][1]

				# store the bigger y
				if maxY < points[i][1]:
						maxY = points[i][1]

		return minY, maxY


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
minY, maxY = boundary(points)
print("min y", minY)
print("max y", maxY)