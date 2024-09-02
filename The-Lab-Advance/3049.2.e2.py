import math

class Circle:

	#class variable
	valid = 0
	invalid = 0

	#stores radius
	def __init__(self, radius):
		self.radius = radius

		if self.radius > 0:
			Circle.valid += 1
		else:
			Circle.invalid += 1

	#area of circle
	def area(self):
		area = math.pi * self.radius * self.radius
		area = round(area,1)
		return area

	#circumference of circle
	def circumference(self):
		circumference = 2 * math.pi * self.radius
		circumference = round(circumference,1)
		return circumference

	#if radius positive, call area() and circumference()
	def display_info(self):
		if self.radius > 0:
			area = self.area()
			circumference = self.circumference()
			print("area",area,"circumference",circumference)

	#display valid and invalid
	def display_valid(self):
		print("valid",Circle.valid,"invalid",Circle.invalid)


#main
circlelist = []
while True:
	radius = input("Input a radius of a circle: ")
	radius = float(radius)

	if radius == 0:
		break
	else:
		radius = Circle(radius)
		circlelist.append(radius)


for i in range(len(circlelist)):
	circlelist[i].display_info()

circlelist[i].display_valid()
