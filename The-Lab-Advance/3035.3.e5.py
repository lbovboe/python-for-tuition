"""
Learning Objectives:
- String operators * +
- If student is stuck, guide them to do the "." and then "#" and join them
"""
# enter integers
nums = input("Input 2 integers: ")
num1, num2 = nums.split()
num1 = int(num1)
num2 = int(num2)

# students may use loops but show them this alternative to shorten it.
# highlight to student this method will be needed in subsequent steps.
print("."*num1 + "#"*num2)