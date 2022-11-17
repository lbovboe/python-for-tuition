
#create 4 unique numbers without duplicate numbers


import random

while True:
    random_list = [ random.randint(0,9) for i in range(4)]
    # print(random_list)
    for i in range(4):
        c = 0
        for j in range(4):
            if random_list[i] == random_list[j]:
                c +=1
        if c>1:
            print('duplicate is found')
            break
 
    if c <= 1:
        print('No duplicate found')
        break



while True:
    bull_count = 0
    cow_count = 0 

    guess_number = input('Enter the 4 unique digit guess number: ')
    guess_number = list(guess_number) # convert into list of digits but still in string format
    guess_number = list(map(int,guess_number)) # convert every string digit to integer
    print(random_list) # for testing purposes can remove this one for ppl to guess
    print(guess_number)

    # check for how many bulls are there
    for i in range(4):
        if guess_number[i] == random_list[i]:
            bull_count += 1
    print('Bull count : ',bull_count)

    # check for how many cows are there
    for i in range(4):
        if guess_number[i] in random_list:
            if guess_number[i] != random_list[i]:
                cow_count += 1
    print('Cow count : ',cow_count)

    if bull_count ==4:
        print('You got it right!')
        break

