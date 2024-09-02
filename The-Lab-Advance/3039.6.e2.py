"""
Learning Objectives:
- Introduction to binary and bits
- Using list to represent binary
"""
# enter number of bits
bits = input("Input number of bits: ")
bits = int(bits)

# create list of 0 to represent binary (should be integer not string)
binary = [0 for i in range(bits)]
print("Binary", binary)
