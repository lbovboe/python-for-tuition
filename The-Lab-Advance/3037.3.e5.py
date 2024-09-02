"""
Learning Objectives:
- Running date and resetting
- Proper sequencing of updating, resetting and display
- If students are stuck, guide to do in order:
		1. check valid date entry <-- done in Qn Date 2, modify to update a flag
		2. loop date:
				increment till Jan end is reached (test with Jan first) <-- done in !n Date 3
				add in other months
				increment year at Dec
"""
import time

#################### CHECK VALID DATE ################################################################
# input date
dmy = input("Input date (D MMM Y): ")
d, m, y = dmy.split()
d = int(d)
y = int(y)

# check months with 31 days
if m == "Jan" or m == "Mar" or m == "May" or m == "Jul" or m == "Aug" or m == "Oct" or m == "Dec":
		if d < 1 or d > 31:
				valid = False
		else:
				valid = True

# check months with 30 days
elif m == "Apr" or m == "Jun" or m == "Sep" or m == "Nov":
		if d < 1 or d > 30:
				valid = False
		else:
				valid = True

# check Feb
elif m == "Feb":
		# leap year
		if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
				if d < 1 or d > 29:
						valid = False
				else:
						valid = True
		# non-leap year
		else:
				if d < 1 or d > 28:
						valid = False
				else:
						valid = True

#################### RUN DATE IF VALID ###############################################################

if valid == False:
		print("Invalid date")
else:
		while True:
				# increase day
				d += 1

				# check if end of month is reached
				if m == "Jan":
						if d == 32:
								d = 1
								m = "Feb"
				elif m == "Feb":
						# leap year
						if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
								if d == 30:
										d = 1
										m = "Mar"
						# non-leap year
						else:
								if d == 29:
										d = 1
										m = "Mar"
				elif m == "Mar":
						if d == 32:
								d = 1
								m = "Apr"
				elif m == "Apr":
						if d == 31:
								d = 1
								m = "May"
				elif m == "May":
						if d == 32:
								d = 1
								m = "Jun"
				elif m == "Jun":
						if d == 31:
								d = 1
								m = "Jul"
				elif m == "Jul":
						if d == 32:
								d = 1
								m = "Aug"
				elif m == "Aug":
						if d == 32:
								d = 1
								m = "Sep"
				elif m == "Sep":
						if d == 31:
								d = 1
								m = "Oct"
				elif m == "Oct":
						if d == 32:
								d = 1
								m = "Nov"
				elif m == "Nov":
						if d == 31:
								d = 1
								m = "Dec"
				elif m == "Dec":
						if d == 32:
								d = 1
								m = "Jan"
								y += 1

				print(d, m, y)
				time.sleep(0.2)