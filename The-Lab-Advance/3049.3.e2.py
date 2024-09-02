class Train:

	#count the total carriages
	total = 0

	#stores number of carriages
	def __init__(self):
		self.num = 0

	#input number and add to total
	def input_num(self):
		self.num = input("number of carriages: ")
		self.num = int(self.num)
		Train.total += self.num

	#display train and total
	#each carriage "#####"
	#if 3 carriage = #####-######-#####
	def display(self):
		#put in first carriage manually
		trainlist =["#####"]
		#put in subsequent carriage
		for i in range(1,int(self.num),1):
			trainlist.append("-#####")
		print(*trainlist,sep="")
		print("Total carriages: ",Train.total)


#main
for i in range(3):
	train = Train()
	train.input_num()
	train.display()