import random

class Superhero:

	#name of characters and stores action of attact or defends
	def __init__(self, name):
		self.name = name
		self.combat = ""

	#decide attack or defend
	def select_combat(self):
		num = random.randint(1,2)
		if num == 1:
			self.combat = "attacks"
		else:
			self.combat = "defends"
		print(self.name, self.combat)


class Arena:
	#static function: enter a hero name and display attack/defend
	@staticmethod
	def main():
		hero = input("Hero name: ")
		hero = Superhero(hero)
		hero.select_combat()


#main
Arena.main()