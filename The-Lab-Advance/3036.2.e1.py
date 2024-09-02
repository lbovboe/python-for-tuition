"""
Learning Objectives:
- practise long manual conversion
- using elif in long checks
- students are NOT ALLOWED to use Python's datetime library
"""
# Enter month in numeric.
# It is optional to convert to integer
m = input("Input month: ")

# If student uses multiple "if" instead of "elif" in a long construct like this,
# explain to them that causes the computer to perform maximum checks each time and
# in a big application, such habit will cause lagging. So apply elif instead.
if m == "1":
		print("Jan")
elif m == "2":
		print("Feb")
elif m == "3":
		print("Mar")
elif m == "4":
		print("Apr")
elif m == "5":
		print("May")
elif m == "6":
		print("Jun")
elif m == "7":
		print("Jul")
elif m == "8":
		print("Aug")
elif m == "9":
		print("Sep")
elif m == "10":
		print("Oct")
elif m == "11":
		print("Nov")
elif m == "12":
		print("Dec")