import math

class Shape:

	def __init__(self):
		self.area = 0

	def display_area(self):
		print("The area is",self.area)


class Square(Shape):

	def __init__(self):
		super().__init__()
		self.length = 0

	#key in length
	def input_length(self):
		length = input("Enter length of square: ")
		self.length = float(length)

	#calculate area of square
	def calculate_area(self):
		self.area = round(self.length * self.length, 2)


class Circle(Shape):

	def __init__(self):
		super().__init__()
		self.radius = 0

	#key in radius
	def input_radius(self):
		radius = input("Enter radius of circle: ")
		self.radius = float(radius)

	#calculate area of circle
	def calculate_area(self):
		self.area = round(math.pi * self.radius * self.radius, 2)


#main
square = Square()
square.input_length()
square.calculate_area()
square.display_area()
circle = Circle()
circle.input_radius()
circle.calculate_area()
circle.display_area()