class Convert:

	#convert inch to cm
	@staticmethod
	def convert(length):
		convert = length*2.54
		convert = round(convert,1)
		print(str(convert)+"cm")

	@staticmethod
	def main():
		while True:
			length = input("Input a length: ")
			if length == "end":
				break
			else: 
				#must iterate to float
				length = float(length)
				Convert.convert(length)

Convert.main()
