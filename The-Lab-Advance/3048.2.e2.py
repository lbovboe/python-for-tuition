class Number:

	#store an integer
	def __init__(self, text):
		self.text = text

	#display the value
	def display(self):
		print(self.text)

	#swap the value
	def swap(self,obj):
		self.temp = self.text
		self.text = obj.text
		obj.text = self.temp

#main
object_1 = input("Enter integer of object1: ")
object_1 = Number(object_1)

object_2 = input("Enter integer of object2: ")
object_2 = Number(object_2)

object_1.display()
object_2.display()

object_1.swap(object_2)

object_1.display()
object_2.display()