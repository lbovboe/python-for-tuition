"""
Learning Objectives:
- File I/O: open file with "r"
- reading until end of file
- If student is stuck, guide the steps in top down order.
"""


def readfile():

		# open file with mode "r"
		with open("data.txt", "r") as f:
				# loop until end of file is detected
				while True:
						text = f.readline().rstrip()

						# check for end of file
						if text == "":
								print("end of file")
								break

						# else display text
						else:
								print(text)


# main ##############################################################
readfile()