import replit
import random
import time

class Racer:

	#max track is 30
	track_length = 30

	#stores racer number and distance travelled
	def __init__(self,num):
		self.racer = num
		self.distance = 0

	#add random number to distance and check if exceed, set to max
	def race(self):
		self.distance += random.randint(1,3)
		if self.distance > Racer.track_length:
			self.distance = 30

	#display the race race_num race_distance ":"
	def display(self):
		#while racing
		#use "+" so it doesn't have extra spacing in between
		if self.distance < Racer.track_length:
			print(" "*self.distance+str(self.racer)+" "*(Racer.track_length-self.distance-1)+":")
		else:
			#when reaches the goal, remove ":"
			print(" "*self.distance+str(self.racer)+" "*(Racer.track_length-self.distance-1))

	#check for winner
	@staticmethod
	def winner(racer_list):
		winner_list = []
		winner = False
		for i in range(len(racer_list)):
			#check if there is any winner in the game
			if racer_list[i].distance==Racer.track_length:
				winner_list.append(racer_list[i].racer)
				winner = True

		if winner == True:
			print("Winner(s):",end="")
			for i in range(len(winner_list)):
				print("Racer",winner_list[i],end=" ")
			return True
		else:
			return False

	@staticmethod
	def main():
		#manually create the object
		racerlist = [Racer(1), Racer(2), Racer(3), Racer(4)]

		replit.clear()

		for i in range(len(racerlist)):
			racerlist[i].display()
		time.sleep(3)

		while True:
			replit.clear()
			for i in range(len(racerlist)):
				racerlist[i].race()

			for i in range(len(racerlist)):
				racerlist[i].display()
			time.sleep(0.3)

			#call the winner
			if Racer.winner(racerlist) == True:
				break

#main
Racer.main()