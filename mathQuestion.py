import random
# digit1 = random.randint(1,1000)
# digit2 = random.randint(1,1000)

while True:
    digit1 = random.randint(1,1000)
    digit2 = random.randint(1,1000)
    question = random.randint(1,4)
    if question == 1:
        print(digit1,'+', digit2,'= ??')
        ans = input('Enter the answer : ')
        ans = int(ans)
        if ans == digit1 + digit2:
            print('correct')
        else:
            print('wrong')
    if question == 2:
        print(digit1,'-', digit2,'= ??')
        ans = input('Enter the answer : ')
        ans = int(ans)
        if ans == digit1 - digit2:
            print('correct')
        else:
            print('wrong')
    if question == 3:
        print(digit1,'x', digit2,'= ??')
        ans = input('Enter the answer : ')
        ans = int(ans)
        if ans == digit1 * digit2:
            print('correct')
        else:
            print('wrong')
    if question == 4:
        if digit1 > digit2:
            print(digit1,'÷', digit2,'= ?? (nearest whole number)')
            ans = input('Enter the answer : ')
            ans = int(ans)
            if ans == digit1 // digit2:
                print('correct')
            else:
                print('wrong')