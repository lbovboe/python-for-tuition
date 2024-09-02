"""
Learning Objectives:
- File I/O: open file with "w"
- using loop within file open
- If student is stuck, guide the steps in top down order.
"""


def save():

		# open file with mode "w" (existing contents will be erased)
		with open("data.txt", "w") as f:
				# loop until "end" is entered
				while True:
						text = input("Enter text: ")

						# break if "end" is entered
						if text == "end":
								break

						# else write to file
						else:
								f.write(text + "\n")


# main ##############################################################
save()