class Number:

	#store list
	def __init__(self,num_list):
		self.num_list = num_list

	#display first and last number
	def display(self):
		print(self.num_list[0],self.num_list[-1])


#main
my_list = input("Enter a list of integers: ")
my_list = my_list.split(" ")
my_list = Number(my_list)
my_list.display()