import random
numbers = []
for i in range(3):
    n = random.randint(1,10)
    numbers.append(n)
total = sum(numbers)
avarage = total/len(numbers)
print('The avarage is :',round(avarage,1))