"""
Learning Objectives:
- Creating list from input
- Checking index within range and accessing values in list
"""
# enter characters and create list
characters = input("Input characters: ")
characters = characters.split()

# display list
print(characters)

# enter indices
indices = input("Input index range (start end): ")
idx_start, idx_end = indices.split()
idx_start = int(idx_start)
idx_end = int(idx_end)

# check index range and display using for-loop
if idx_start >= 0 and idx_end < len(characters):
		for i in range(idx_start, idx_end + 1, 1):
				print(characters[i], end=" ")
else:
		print("index out of range")