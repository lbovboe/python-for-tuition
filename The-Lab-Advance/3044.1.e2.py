"""
Learning Objectives:
- File I/O: open file with "w"
- If student is stuck, guide the steps in top down order.
"""

# input filename
filename = input("Input filename: ")

# open file with mode "w" (existing contents will be erased)
with open(filename, "w") as f:
		# upon the open command, cannot leave blank so place the print statement here.
		print("file created")