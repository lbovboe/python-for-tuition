class Number:

	#store a list
	def __init__(self, my_list):
		self.num_list = my_list

	#display
	def display(self):
		print(*self.num_list)

	#addition
	def add(self,num):
		for i in range(len(self.num_list)):
			self.num_list[i] = int(self.num_list[i])
			self.num_list[i] += num


#main
my_list = input("Enter a list of integers: ")
my_list = my_list.split(" ")
my_list = Number(my_list)
my_list.display()
my_list.add(5)
my_list.display()
my_list.add(-3)
my_list.display()