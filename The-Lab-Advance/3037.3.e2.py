"""
Learning Objectives:
- Determining valid date via multiple conditions
- Using AND/OR or nested ifs are both acceptable
- If students are stuck, guide them to do Jan and test first.
- Then let them try adding in the rest.
- Do Feb last, after the other months are working.
"""
# input date
dmy = input("Input date (D MMM Y): ")
d, m, y = dmy.split()
d = int(d)
y = int(y)

# Most students tend to:
#   - check for "out of range" with nested if
#   - use separate if statement for each month (guide them to combine using OR)
# They are allowed to use any logic constructs as long as it can produce the right answer

# check months with 31 days
if m == "Jan" or m == "Mar" or m == "May" or m == "Jul" or m == "Aug" or m == "Oct" or m == "Dec":
		if d < 1 or d > 31:
				print("invalid")
		else:
				print("valid")

# check months with 30 days
elif m == "Apr" or m == "Jun" or m == "Sep" or m == "Nov":
		if d < 1 or d > 30:
				print("invalid")
		else:
				print("valid")

# check Feb
elif m == "Feb":
		# leap year
		if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
				if d < 1 or d > 29:
						print("invalid")
				else:
						print("valid")
		# non-leap year
		else:
				if d < 1 or d > 28:
						print("invalid")
				else:
						print("valid")

# this is optional as we assume valid month name is entered
else:
		print("invalid")