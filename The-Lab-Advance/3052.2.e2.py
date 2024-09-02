#Method1
string = input("Enter string: ")
substring = input("Enter substring: ")

#if cannot find existence of substring, return -1
#not equal to -1 means found the substring in the string
if string.find(substring) != -1:

	#find() will return the index value of the first occurrence when found
	index = string.find(substring)

	#convert to string to replace the substring with "-"
	string = list(string)
	for i in range(len(substring)):
		string[index] = "-"
		index += 1

	#display the list without spaces
	print(*string, sep="")

else:
	print(string)

##########################################################################

#Method2
# enter string and search string
text = input("Enter string: ")
substring = input("Enter substring: ")

# use find() to find index of first occurrence of substring
index = text.find(substring)

##########################################################################
# longer method is to cast to list and replace ###########################
##########################################################################
if index != -1:
		text = list(text)
		for i in range(index, index+len(substring)):
				text[i] = "-"
		text = "".join(text)
print(text)

##########################################################################
# shorter method using string index $$$$$$$###############################
##########################################################################
# if index != -1:
#     text = text[:index] + "-"*len(substring) + text[index+len(substring):]
# print(text)