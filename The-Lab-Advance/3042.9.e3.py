"""
Learning Objectives:
- Learn about collision detection: point intersecting within rectangle
- When students are stuck, follow the steps in the solution in the order
		main
		boundary()
		intersect()
"""


# function to find min x, max x, min y and max y values from a list of points (boundaries box).
# this is from previous challenge.
def boundary(points):

		# set min and max to first x and iterate through remaining list
		minX = points[0][0]
		maxX = points[0][0]
		minY = points[0][1]
		maxY = points[0][1]
		for i in range(1, len(points)):

				# store the smaller x
				if minX > points[i][0]:
						minX = points[i][0]

				# store the bigger x
				if maxX < points[i][0]:
						maxX = points[i][0]

				# store the smaller y
				if minY > points[i][1]:
						minY = points[i][1]

				# store the bigger y
				if maxY < points[i][1]:
						maxY = points[i][1]

		return minX, maxX, minY, maxY


# function to find intersection of point within a box (2D list of 4 points)
# it is acceptable if student pass in the parameters differently
def intersect(cannon, box):

		# get castle boundaries
		minX, maxX, minY, maxY = boundary(box)

		# check cannon within boundaries
		if cannon[0] >= minX and cannon[0] <= maxX and cannon[1] >= minY and cannon[1] <= maxY:
				return "hit"
		else:
				return "not hit"


# main #####################################################

# enter cannon ball point
cannon = input("Enter coordinate of cannon ball: ")
cannon = cannon.split(",")
cannon[0] = float(cannon[0])
cannon[1] = float(cannon[1])

# enter boundaries
box = input("Enter boundary of castle: ")
box = box.split()
# using loop to split and cast
# it is acceptable that student do the long way without loop
for i in range(4):
		box[i] = box[i].split(",")
		box[i][0] = float(box[i][0])
		box[i][1] = float(box[i][1])

# check intersection and display result
result = intersect(cannon, box)
print(result)