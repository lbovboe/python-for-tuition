"""
Learning Objectives:
- Function: function with parameters and return values
- calling function with variables as parameter and receiving return values
- understanding data type of parameters
- When students are stuck, guide in steps
		scoring()
		main
"""


def scoring(score1, score2):
		# student may also calculate and return directly
		total = score1 + score2
		average = total/2
		return total, average


# main ########################################

# enter scores
scores = input("Input 2 scores: ")
score1, score2 = scores.split()
score1 = int(score1)
score2 = int(score2)

# call function and display results
total, average = scoring(score1, score2)
print("total", total)
print("average", average)