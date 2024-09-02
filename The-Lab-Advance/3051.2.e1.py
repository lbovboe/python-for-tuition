class Shape:

	#store area
	def __init__(self):
		self.area = 0

	#display the area
	def display(self):
		print("The area is",self.area)

class Square(Shape):

	#store length
	def __init__(self,length):
		super().__init__()
		self.length = length

	#calculate area
	def calculate_area(self):
		self.area = self.length * self.length

#main
length = input("Enter length of square: ")
length = float(length)
square = Square(length)
square.calculate_area()
square.display()