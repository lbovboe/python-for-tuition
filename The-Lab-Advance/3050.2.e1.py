import replit
import time

class Racer:

	#max track length
	track_length = 30

	#store the distance
	def __init__(self):
		self.distance = 0

	def race(self):
		self.distance +=1

	#display position of the racer
	def display(self):
		print(" "*self.distance,"R")

	def reach(self):
		if self.distance == Racer.track_length:
			return True
		else:
			return False

	@staticmethod
	def main():
		racer = Racer()

		replit.clear()
		racer.display()
		time.sleep(3)

		while True:
			if racer.reach() == True:
				break
			else:
				replit.clear()
				racer.race()
				racer.display()
				time.sleep(0.3)
				racer.reach()

#main
Racer.main()
