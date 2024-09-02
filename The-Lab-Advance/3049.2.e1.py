class Circle:

	#positive is valid, negative is invalid
	valid = 0
	invalid = 0

	#radius in float
	def __init__(self, radius):
		self.radius = radius

		if self.radius > 0:
			Circle.valid += 1
		else:
			Circle.invalid += 1

	#display radius
	def display_radius(self):
		print("radius",self.radius)

	#display valid/invalid
	def display_valid(self):
		print("valid "+str(Circle.valid)+" invalid "+str(Circle.invalid))

#main
radiuslist =[]
while True:
	radius = input("Input a radius of a circle: ")
	radius = float(radius)

	if radius == 0:
		break

	else:
		radius = Circle(radius)
		radiuslist.append(radius)

for i in range(len(radiuslist)):
	radiuslist[i].display_radius()

radiuslist[0].display_valid()