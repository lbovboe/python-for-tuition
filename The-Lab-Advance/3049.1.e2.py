class Car:

	#class variable
	count = 0

	#store brand and colour
	def __init__(self, brand, colour):
		self.brand = brand
		self.colour = colour
		Car.count += 1

	#display
	def display(self):
		print(self.brand,self.colour,Car.count)

#main
carlist =[]
while True:
	carbrand = input("Input car brand: ")
	if carbrand == "end":
		break

	carcolour = input("Input car colour: ")
	car = Car(carbrand, carcolour)
	carlist.append(car)

#when every object is created, class variable is increased
#it is a good habit to use the latest object value
for i in range(len(carlist)):
	carlist[i].display()