class Text:

	#store a string
	def __init__(self, text):
		self.text = text

	#display the text
	def display(self):
		print(self.text)

	#copy value
	def copy(self,obj):
		self.text = obj.text

#main
object_1 = input("Enter a text of object 1: ")
object_1 = Text(object_1)

object_2 = input("Enter a text of object 2: ")
object_2 = Text(object_2)

object_1.display()
object_2.display()

object_1.copy(object_2)

object_1.display()
object_2.display()