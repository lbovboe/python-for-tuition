"""
Learning Objectives:
- Try-exception : error caused by casting
- When students are stuck, guide in steps
		creating the try exception
		putting in loop
"""
while True:
		try:
				# input and cast
				nums = input("Input 2 float numbers (x y): ")
				x, y = nums.split()
				x = float(x)
				y = float(y)

				# display. do not need to check y==0 as it will trigger an error
				print(x/y)
				break
		except:
				print("invalid")