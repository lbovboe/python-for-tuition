"""
Learning Objectives:
- calculating leap year
"""
# input year
year = input("Input year: ")
year = int(year)

# Students may also combine the conditions below using OR

# div by 4 but not 100
if year % 4 == 0 and year % 100 != 0:
		print("leap year")
# div 400
elif year % 400 == 0:
		print("leap year")
else:
		print("not leap year")
