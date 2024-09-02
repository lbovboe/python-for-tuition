"""
Learning Objectives:
- File I/O: file pointer position (tell and seek at right location)
- Understanding file mode that allows read and write
- If student is stuck, guide the steps in top down order.
"""


def replace():

		# open file with mode "r"
		with open("data.txt", "r+") as f:
				# loop until end of file is detected
				while True:
						# remember the position BEFORE reading
						position = f.tell()
						text = f.readline().rstrip()

						# check for end of file
						if text == "":
								break

						# if matches search string, write string at the position
						elif text == "Hello there!":
								f.seek(position)
								f.write("yellow melon")


# main ##############################################################
replace()