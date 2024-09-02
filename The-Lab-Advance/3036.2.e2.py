"""
Learning Objectives:
- practise long manual conversion
- using elif in long checks
- using split appropriately
- customising input message with counter
- students are NOT ALLOWED to use Python's datetime library
"""
# enter qty
num = input("How many dates are there: ")
num = int(num)

# loop
for i in range(0, num, 1):
		# enter date
		dmy = input("Input date " + str(i+1) + " (D/M/Y): ")
		d, m, y = dmy.split("/")

		# If student uses multiple "if" instead of "elif" in a long construct like this,
		# explain to them that causes the computer to perform maximum checks each time and
		# in a big application, such habit will cause lagging. So apply elif instead.
		#
		# Students will tend to use print directly inside the if statement.
		# This is allowed but explain to student that in the event you want to change
		# the display format, he will need to change all of them so it is less flexible.
		if m == "1":
				m = "Jan"
		elif m == "2":
				m = "Feb"
		elif m == "3":
				m = "Mar"
		elif m == "4":
				m = "Apr"
		elif m == "5":
				m = "May"
		elif m == "6":
				m = "Jun"
		elif m == "7":
				m = "Jul"
		elif m == "8":
				m = "Aug"
		elif m == "9":
				m = "Sep"
		elif m == "10":
				m = "Oct"
		elif m == "11":
				m = "Nov"
		elif m == "12":
				m = "Dec"

		print(d, m, y)