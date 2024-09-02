"""
Learning Objectives:
- File I/O: working with multiple files
- Creating reusable functions for File I/O
- If student is stuck, guide the steps:
		save()
		read()
		main
"""


def save(filename):

		print("Recording", filename)

		# open file with mode "w" (existing contents will be erased)
		with open(filename, "w") as f:
				# loop until "end" is entered
				while True:
						text = input("Enter text: ")

						# break if "end" is entered
						if text == "end":
								break

						# else write to file
						else:
								f.write(text + "\n")


def read(filename):

		# open file with mode "r"
		with open(filename, "r") as f:
				# loop until end of file is detected
				while True:
						text = f.readline().rstrip()

						# check for end of file
						if text == "":
								break

						# else display text
						else:
								print(text)


# main ##############################################################
save("data1.txt")
save("data2.txt")
read("data1.txt")
read("data2.txt")