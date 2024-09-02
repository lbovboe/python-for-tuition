class Bird:

	#species and colours
	def __init__(self, species, colour):
		self.species = species
		self.colour = colour

	#display colour then species
	def display(self):
		print(self.colour,self.species)


#main
species = input("Input bird species: ")
colour = input("Input bird colour: ")
bird = Bird(species, colour)
bird.display()