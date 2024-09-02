class Train:

	#total carriage and size
	total_carriage = 0
	total_size = 0

	#stores a list of carriages size
	#size means each carriage contains different number of "#"
	def __init__(self):
		self.carriage_list =[]

	#input list
	def input_list(self):
		carriage = input("Input carriage sizes (1-10): ")
		self.carriage_list = carriage.split(" ")

		#update the total carriage
		#meaning how many item in the list
		Train.total_carriage += len(self.carriage_list)

		#update the total size
		#meaning how many "#"
		for i in range(len(self.carriage_list)):
			self.carriage_list[i] = int(self.carriage_list[i])
			Train.total_size += self.carriage_list[i]

	#display
	def display(self):
		#print out the first carriage
		print("#"*self.carriage_list[0],end="")
		#print out the subsequence carriages
		for i in range(1,len(self.carriage_list)):
			print("-"+"#"*self.carriage_list[i],end="")
		print()
		print("Total carriage",Train.total_carriage)
		print("Total size",Train.total_size)

for i in range(2):
	train = Train()
	train.input_list()
	train.display()