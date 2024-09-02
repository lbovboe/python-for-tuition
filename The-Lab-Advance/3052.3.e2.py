
class EnglishDigit:

	#initialise a dictionary as an object
	def __init__(self):
		self.digit = { "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine" }

	#give instructions according to language
	def input_digit(self):
		self.num = input("Enter a digit 0-9: ")

	#return value from dictionary
	def show_digit(self):
		print(self.digit[self.num])

class FrenchDigit(EnglishDigit):

	def __init__(self):
		self.digit = { "0": "zéro", "1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq", "6": "six", "7": "sept", "8": "huit", "9": "neuf" }

	def input_digit(self):
		self.num = input("Entrez un chiffre 0-9: ")


class ChineseDigit(EnglishDigit):

	def __init__(self):
		self.digit = { "0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九" }

	def input_digit(self):
		self.num = input("输入数字 0-9: ")

while True:
	print( "[1] English  [2] Français  [3] 中文" )
	language = input("Enter language: ")

	if language == "1":
			digit = EnglishDigit()
	elif language == "2":
			digit = FrenchDigit()
	elif language == "3":
			digit = ChineseDigit()

	digit.input_digit()
	digit.show_digit()
