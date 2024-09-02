"""
Learning Objectives:
- Introduction to binary and bits
- Implementing algorithm to counting binary number
- Students are stuck, guide in steps following the order in solution.
"""
# enter number of bits
bits = input("Input number of bits: ")
bits = int(bits)

# calculate
num_bin = 2**bits

# create binary
binary = [0 for i in range(bits)]

# loop to count perform binary counting
for i in range(num_bin):

		# display binary
		print(i, "=", *binary)

		# Step 1: Add 1 to last bit
		binary[len(binary)-1] += 1

		# Step 2: Check carry over from last to 1st bit
		for j in range(len(binary)-1, 0, -1):

				# carry over
				if binary[j] == 2:
						binary[j] = 0
						binary[j-1] += 1

				# break and do next count if no carry over.
				# Carry over ripples from the last bit towards the 1st,
				# so when the carry over stops at one bit,
				# it means the remaining bits will not have any carry over.
				else:
						break

