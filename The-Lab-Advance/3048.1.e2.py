class Friend:

	#stores name of friend
	def __init__(self, name):
		self.name = name

	#display the name
	def display(self):
		print(self.name)


#main
name = input("Enter name: ")
friend = Friend(name)
friend.display()

