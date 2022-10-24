import random
print('Select 1 --> Generating a random number answer')
print('Select 2 --> Key in your own answer number')

choice = int(input('Enter your choice : '))


if choice == 1:
    answer = random.randint(1,99)
else:
    answer = int(input('Enter your answer : '))

    # Make 100 lines so other users can't see the answer
    for i in range(100):
        print()

while True:
    guess_number = int(input('Enter your guess number : '))
    if answer > guess_number:
        print('The answer is bigger than your guess number')
    elif answer < guess_number:
        print('The answer is smaller than your guess number')
    else:
        print('Your are correct! :D')
        break
    
