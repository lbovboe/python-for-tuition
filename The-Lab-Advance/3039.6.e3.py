"""
Learning Objectives:
- Introduction to binary and bits
- Determining the number of patterns
"""
# enter number of bits
bits = input("Input number of bits: ")
bits = int(bits)

# calculate and display number of patterns
num_bin = 2**bits
print(num_bin, "patterns")