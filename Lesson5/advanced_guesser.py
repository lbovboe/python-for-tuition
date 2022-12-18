import random
import time
word_pool = []
d = {}
number_players = int(input('Enter the number of players : '))

for i in range(number_players):
    name = input('Enter name '+str(i+1) + ' :')
    d[name] = 0

print(d)
# creating a pool of words
# while True:
#     word = input('Enter word for dictionary: ')
#     if word =='end':
#         break
#     word_pool.append(word)
with open('dictionary.txt') as f:
    while True:
        lines = f.readline().rstrip()
        if lines == '':
            break
        word_pool.append(lines)
        
    

while True:
    # choose a random word from the word_pool
    for i in range(100):
        print()
    total_number_words = len(word_pool)
    random_word = word_pool[random.randint(0,total_number_words-1)]

    # print out the dash mat for guessing
    word_length = len(random_word)
    guesser_container = ['-' for i in range(word_length)]
    print(*guesser_container)
    print()

    # set lives to 5
    

    lives = 5
    keys = list(d.keys())
    while True:
        for key in keys:
            while True:
                if d[key] > 5 : 
                    print('Currently you earned : ' , d[key]//5, 'coins')
                alphabet = input('Enter your guess alphabet/word : ')
                
                # if the user only entered 1 letter
                if len(alphabet) == 1:
                    if alphabet in random_word:
                        # find the indexes that appear inside this random word
                        for i in range(word_length):
                            if alphabet == random_word[i]:
                                guesser_container[i] = alphabet
                    else:
                        print('Wrong guess ! Guess Again.')
                        lives-=1
                        print('Remaining Lives : ', lives)
                else:
                    # when user wants to key in the whole word
                    if random_word == alphabet:
                        print('-------You Won ------')
                        d[key] +=1
                        print('The answer is : ', random_word)
                        print("Your Current Score is : ", score)
                        for i in range(3,0,-1):
                            print('Next question in',i+1,'seconds')
                            time.sleep(1)
                        break
                    else:
                        print('Wrong guess ! Guess Again.')
                        lives-=1
                        print('Remaining Lives : ', lives)

                        
                
                print(*guesser_container)
                # break when all the dash are filled up
                if '-' not in  guesser_container:
                    d[key] +=1
                    print('-------You Won ------')
                    print('The answer is : ', random_word)
                    print("Your Current Score is : ", score)
                    for i in range(3,0,-1):
                        print('Next question in',i+1,'seconds')
                        time.sleep(1)
                    break
                if lives == 0:
                    print("----You Lost No more Lives -----")
                    print('The answer is : ', random_word)
                    print("Your Current Score is : ", score)
                    for i in range(3,0,-1):
                            print('Next question in',i+1,'seconds')
                            time.sleep(1)
                    break