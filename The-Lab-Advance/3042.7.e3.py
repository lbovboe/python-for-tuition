"""
Learning Objectives:
- Learn about Cartesian Coordinates: comparing points to check for shapes
- When students are stuck, follow the steps in the solution in the order
		main
		square()
"""


# function check if it is a square
def square(ptA, ptB, ptC, ptD):

		# if students use many AND to chain up many conditions,
		# teach them to use NESTED IFs for neatness and easier debugging

		# SQUARE ##################################################################
		# pointA(x, y)┎-------┒pointB(x, y)
		# pointD(x, y)┖-------┚pointC(x, y)
		# AB and DC are horizontal
		# and AD and BC are vertical
		# and 2 adjacent lengths are the same

		# check AB is horizontal
		if ptA[0] != ptB[0] and ptA[1] == ptB[1]:

				# check DC is horizontal
				if ptC[0] != ptD[0] and ptC[1] == ptD[1]:

						# check AD is vertical
						if ptA[0] == ptD[0] and ptA[1] != ptD[1]:

								# check BC is vertical
								if ptB[0] == ptC[0] and ptB[1] != ptC[1]:

										# check absolute length of AB and AD are equal
										if ptB[0]-ptA[0] == ptA[1]-ptD[1]:
												# it is a square if all the above are True
												return True

		# if True is not returned, return False
		return False


# main ###############################################


# better students may use 2D list with loop to cast
# points = []
# for i in range(4):
#    pt = input("Enter point " + str(i+1) + " (x,y): ")
#    pt = point.split()
#    pt[0] = float(pt[0])
#    pt[1] = float(pt[1])
#    points.append(pt)
#
# but mostly tend to do it the long way shown below.

# enter point1
point = input("Enter point 1 (x,y): ")
ptA = point.split(",")
ptA[0] = float(ptA[0])
ptA[1] = float(ptA[1])

# enter point2
point = input("Enter point 2 (x,y): ")
ptB = point.split(",")
ptB[0] = float(ptB[0])
ptB[1] = float(ptB[1])

# enter point3
point = input("Enter point 3 (x,y): ")
ptC = point.split(",")
ptC[0] = float(ptC[0])
ptC[1] = float(ptC[1])

# enter point4
point = input("Enter point 4 (x,y): ")
ptD = point.split(",")
ptD[0] = float(ptD[0])
ptD[1] = float(ptD[1])

# check and display result
result = square(ptA, ptB, ptC, ptD)
print(result)