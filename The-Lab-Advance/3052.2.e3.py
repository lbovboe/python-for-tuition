class NumOperation:

	#stores 2 strings
	def __init__(self,x,y):
		self.x = x
		self.y = y

	#addition
	def add(self):
		if self.x.isdigit() and self.y.isdigit():
			self.x = int(self.x)
			self.y = int(self.y)
		result = self.x + self.y
		print(str(self.x) + " + " + str(self.y) + " = " + str(result))

	#subtraction
	def subtract(self):
		self.x = int(self.x)
		self.y = int(self.y)
		result = self.x - self.y
		print(str(self.x) + " - " + str(self.y) + " = " + str(result))


class StrOperation(NumOperation):

	def __init__(self, x, y):
		super().__init__(x, y)

	#overides subtraction
	def subtract(self):
		if self.x.find(self.y) != -1:

			#find() will return the index value of the first occurrence when found
			index = self.x.find(self.y)

			#convert to string and remove the substring
			newlist = list(self.x)
			#remove from backwards
			for i in range((index+len(self.y)-1),(index-1),-1):
				newlist.pop(i)

			#------------------------------
			#remove from front is easier
			#for i in range(len(self.y)):
				#string.pop(index)
			#------------------------------
				
			newlist = "".join(newlist)
			
			#display the result
			print(self.x, "-",self.y,"=",newlist)

		else:
			print(self.x, "-",self.y,"=",self.x)

#main
x = input("enter x: ")
y = input("enter y: ")
if x.isdigit() and y.isdigit():
	equation = NumOperation(x,y)
	equation.add()
	equation.subtract()
else:
	strings = StrOperation(x,y)
	strings.add()
	strings.subtract()



#####################################################
#Method2

class NumOperation:

		def __init__(self, a, b):
				# initialise variables as integers
				self.x = int(a)
				self.y = int(b)

		def add(self):
				# return sum
				return self.x + self.y

		def subtract(self):
				# return difference
				return self.x - self.y


class StrOperation(NumOperation):

		def __init__(self, a, b):
				# skipped calling parent init as it needs integer arguments
				# below overwrites the variables by using same names
				# parent methods can still operate on them
				self.x = a
				self.y = b

		def subtract(self):
				# find the first occurrence of y in x
				index = self.x.find(self.y)

				# if found, remove y from x manually
				# note that students are not taught replace() for string
				if index != -1:
						string = list(self.x)
						for i in range(len(self.y)):
								string.pop(index)
						return ''.join(string)

				# else return original x
				else:
						return self.x


# main #############################################
while True:
		# enter x and y
		x = input("Enter x: ")
		y = input("Enter y: ")

		# if x and y are digits, instance NumOperation
		if x.isdigit() and y.isdigit():
				op = NumOperation(x, y)

		# else instance StrOperation
		else:
				op = StrOperation(x, y)

		# print add and substract
		print(x, '+', y, '=', op.add())
		print(x, '-', y, '=', op.subtract())