import random         

random_list = [ random.randint(0,10) for i in range(5)]
print(random_list)
# get the input and convert to integer at the same time
number = int(input('Enter a number : '))

if number in random_list:
    print('Found')
else:
    print('Not Found')

