"""
Learning Objectives:
- Function: function with parameter and return values
- calling function with list as parameter and receiving return values
- understanding data type of parameter
- When students are stuck, guide in steps
		scoring()
		main
"""


def scoring(scorelist):
		# student may cast to float within the function instead of in main
		# student may also use the built-in function sum()
		total = 0
		for i in range(len(scorelist)):
				total += scorelist[i]

		# calculate average and round to whole number
		average = total/len(scorelist)
		average = round(average)

		# calculate grade
		if average > 75:
				grade = "distinction"
		elif average >= 50 and average <= 75:
				grade = "moderate"
		else:
				grade = "fail"

		return average, grade


# main ########################################

# enter scores
scores = input("Input scores: ")

# split into list and cast to floats
scorelist = scores.split()
for i in range(len(scorelist)):
		scorelist[i] = float(scorelist[i])

# call function and display result
average, grade = scoring(scorelist)
print("average", average)
print("grade", grade)