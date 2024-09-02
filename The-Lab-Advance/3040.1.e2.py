"""
Learning Objectives:
- Try-exception : error caused by casting
- When students are stuck, guide in steps
		creating the try exception
		checking range
		putting in loop
"""
while True:
		try:
				# input and cast
				num = input("Input negative integer: ")
				num = int(num)

				# check negative range
				if num < 0:
						print("valid")
						break
				else:
						print("invalid")
		except:
				print("invalid")