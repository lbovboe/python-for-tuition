class Train:

	#count the total carriage
	total = 0

	#name of the train
	def __init__(self):
		self.name = ""

	#input name and count the carriage
	def input_name(self):
		self.name = input("Train name: ")
		Train.total += 3

	#display name and count
	def display(self):
		print(self.name,Train.total)

#main
for i in range(3):
	train = Train()
	train.input_name()
	train.display()
