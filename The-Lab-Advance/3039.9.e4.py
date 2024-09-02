"""
Learning Objectives:
- Character code: accessing every character in a string and convert it to code with ord()
"""
# enter string
message = input("Input message: ")
message = list(message)

for i in range(0, len(message), 1):
		code = ord(message[i])
		code += 1
		message[i] = chr(code)

encrypted = "".join(message)
print(encrypted)