numbers = input("Enter a line of numbers: ").split()
total = 0
for i in range(len(numbers)):
    total += float(numbers[i])
print('The total is:',total)
