class Convert:

	@staticmethod
	def convert(length):
		#check if cm, convert to inch
		#use slicing is easier
		if length[-2:] == "cm":
			new_length = float(length[:-2])*0.3937
			new_length = round(new_length,1)
			print(str(new_length)+"inch")
		#check if inch, convert to cm
		if length[-4:] == "inch":
			new_length = float(length[:-4])*2.54
			new_length = round(new_length,1)
			print(str(new_length)+"cm")

	@staticmethod
	def main():
		while True:
			length = input("Input length: ")
			if length == "end":
				break
			else:
				Convert.convert(length)

#main
Convert.main()