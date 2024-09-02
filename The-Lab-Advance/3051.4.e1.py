class Human:

	#store name and gender
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender


class Mutant(Human):

	#stores number of mutants
	count = 0

	#add superpower
	def __init__(self, name, gender, superpower):
		super().__init__(name, gender)
		self.superpower = superpower
		Mutant.count += 1

	#create a file and add date
	def record(self):
		#use "a" to append. "w" will overwites the file
		with open("data.txt","a") as f:
			#use "\n" so it break to second line
			f.write(self.name+","+self.gender+","+self.superpower+"\n")

	#display info from a file and count of mutants
	@staticmethod
	def display():
		with open("data.txt","r") as f:
			while True:
				text = f.readline().rstrip()
				if text == "":
					break
				else:
					print(text)
		print(str(Mutant.count),"mutant(s)")


	@staticmethod
	def main():
		number = 1
		while True:
			print("Mutant #"+str(number))
			name = input("Input name: ")
			if name == "end":
				break

			else:
				gender = input("Input gender: ")
				superpower = input("Input superpower: ")
				mutant = Mutant(name, gender, superpower)
				mutant.record()
				number += 1

		Mutant.display()



#main
Mutant.main()