"""
Learning Objectives:
- File I/O: opening multiple files concurrently
- If student is stuck, guide the steps:
		save()
		merge()
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


def merge():

		# open file for writing
		with open("merge.txt", "w") as f:
				# open files for reading
				with open("data1.txt", "r") as f1:
						with open("data2.txt", "r") as f2:
								# loop until end of both files are detected
								while True:
										# read a line from each file.
										# it is fine to continue reading a file even
										# when it has reached its end.
										text1 = f1.readline().rstrip()
										text2 = f2.readline().rstrip()

										# check for end of file
										if text1 != "":
												f.write(text1 + "\n")
										if text2 != "":
												f.write(text2 + "\n")

										# exit when both end of both files are reached
										if text1 == "" and text2 == "":
												break


# main ##############################################################
save("data1.txt")
save("data2.txt")
merge()