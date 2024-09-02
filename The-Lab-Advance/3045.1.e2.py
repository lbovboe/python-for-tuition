"""
Learning Objectives:
- File I/O: file pointer position
- If student is stuck, guide the steps in top down order.
"""


def search():

		# enter search string
		search_str = input("Search string: ")

		# open file with mode "r"
		with open("data.txt", "r") as f:
				# loop until end of file is detected
				while True:
						# remember the position BEFORE reading
						position = f.tell()
						text = f.readline().rstrip()

						# check for end of file
						if text == "":
								break

						# if matches search string, display the start position
						elif search_str == text:
								print(position)


# main ##############################################################
search()