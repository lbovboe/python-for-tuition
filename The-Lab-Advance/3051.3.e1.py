import math

class Square:
	#store length
	def __init__(self, length):
		self.length = length
	#calculate square are
	def square_area(self):
		square_area = self.length * self.length
		return square_area


class Circle:
	#store radius
	def __init__(self, radius):
		self.radius = radius
	#calculate circle area
	def circle_area(self):
		circle_area = math.pi * self.radius * self.radius
		return circle_area


class Shape(Square,Circle):
	#inherit 2 classes
	def __init__(self,length,radius):
		Square.__init__(self, length)
		Circle.__init__(self, radius)
	#calculate the total
	def total_area(self):
		self.total_area = round(self.square_area() + self.circle_area(), 2)
		print("Total area is", self.total_area)


#main
length = float(input("Input length of square: "))
radius = float(input("Input radius of circle: "))
shape = Shape(length,radius)
shape.total_area()