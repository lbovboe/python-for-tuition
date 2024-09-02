import random

class Superhero:

	#stores hero and combat--attack or defend
	def __init__(self,name):
		self.name = name
		self.combat = ""

	#select attack or defends
	def select_combat(self):
		num = random.randint(1,2)
		if num == 1:
			self.combat = "attacks"
		else:
			self.combat = "defends"
		return self.combat

class Arena:

	@staticmethod
	def fight(hero_list):
		for i in range(3):
			#get 1st random number
			randomnum = random.randint(0,len(hero_list)-1)

			#get 2nd random number
			while True:
				randomnum2 = random.randint(0,len(hero_list)-1)
				if randomnum2 != randomnum:
					break

			#choose random hero to fight
			action1 = hero_list[randomnum].select_combat()
			action2 = hero_list[randomnum2].select_combat()

			#display the result
			print(hero_list[randomnum].name,action1,"vs",hero_list[randomnum2].name,action2)

	@staticmethod
	def main():
		herolist=[]
		#input a hero
		while True:
			hero = input("Hero name: ")
			if hero == "end":
				break

			hero = Superhero(hero)
			herolist.append(hero)

		Arena.fight(herolist)



#main
Arena.main()