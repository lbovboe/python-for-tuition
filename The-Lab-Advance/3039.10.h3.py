"""
Learning Objectives:
- Learn about string manipulation with list: matching & substring
- When students are stuck, guide in steps
		inputting
		detecting data and saving
		detecting question
		searching exact match
		searching substring
"""

# record is a list that stores each input as a string
record = []
while True:

		# enter input
		text = input("Input: ")
		if text == "end":
				break
		else:
				# if last character is a "?" then it is a question
				if text[-1] == "?":
						# using string manipulation taught in the notes to remove "?"
						text = text[:-1]

						# break into word list and words[2] is the input subject
						words = text.split()
						subject = words[2]

						# iterate through record to find if input subject exists
						found = False
						for i in range(len(record)):
								# split each record item into word list
								# first word is the record subject
								# last word is the type (number or word)
								recWords = record[i].split()

								# check for exact match
								if subject == recWords[0]:
										found = True
										print(recWords[3])
										break

						# if exact match not found, check substring existence
						if not found:
								for i in range(len(record)):
										# split each record item into word list
										# first word is the record subject
										# last word is the type (number or word)
										recWords = record[i].split()

										# check if input subject is part of record subject or vice versa
										if subject in recWords[0] or recWords[0] in subject:
												found = True
												print("likely", recWords[3])
												break

						# if still not found, display idk
						if not found:
								print("idk")

				# input is a data, append to record list
				else:
						record.append(text)
						print("learning")
