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