import random
import time

class Superhero:

	#stores name, atteack, defence and combat
	def __init__(self, name, attack, defend):
		self.name = name
		self.attack = attack
		self.defence = defend
		self.combat = ""


	#choose attack or defence randomly
	def select_combat(self):
		num = random.randint(1,2)
		if num == 1:
			self.combat = "attacks"
		else:
			self.combat = "defends"


class Arena:

		@staticmethod
		def fight(hero_list):
			#choose random 2 heroes
			random1 = random.randint(0,len(hero_list)-1)

			while True:
				random2 = random.randint(0, len(hero_list)-1)
				if random2 != random1:
					break

			#call their combat action
			hero_list[random1].select_combat()
			hero_list[random2].select_combat()

			#save combat power base on combat action
			if hero_list[random1].combat == "attacks":
				combat_power1 = hero_list[random1].attack
			else:
				combat_power1 = hero_list[random1].defence

			if hero_list[random2].combat == "attacks":
				combat_power2 = hero_list[random2].attack
			else:
				combat_power2 = hero_list[random2].defence

			#display result
			hero1 = hero_list[random1].name
			action1 = hero_list[random1].combat
			hero2 = hero_list[random2].name
			action2 = hero_list[random2].combat
			print(hero1,action1,combat_power1,"vs",hero2,action2,combat_power2)

			#check winner
			if (action1 == "defends" and action2 == "defends") or (combat_power1 == combat_power2):
				print("tie")
			elif combat_power1 > combat_power2:
				print(hero1,"wins")
			else:
				print(hero2,"wins")

			time.sleep(1)


		@staticmethod
		def main():
			herolist = []

			while True:
				#insert hero name
				name = input("Hero name: ")
				if name == "end":
					break

				#insert attack power
				power = input("Attack power (1 to 9): ")
				power = int(power)
				defend = 10 - power

				#create an object
				hero = Superhero(name,power,defend)

				#save into a list
				herolist.append(hero)

			#call fight
			for i in range(3):
				Arena.fight(herolist)

#main
Arena.main()