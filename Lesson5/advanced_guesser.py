import random
import time
import copy
word_pool = []
d = {}
for i in range(100):
    print()
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
# with open('test.txt') as f:
#     while True:
#         lines = f.readline().rstrip()
#         if lines == '':
#             break
#         word_pool.append(lines)
        
    

while True:
    # choose a random word from the word_pool
    temp = copy.deepcopy(d)
    # lives_temp = copy.deepcopy(lives)
    print(temp)

    for i in range(100):
        print()
    total_number_words = len(word_pool)
    random_word = word_pool[random.randint(0,total_number_words-1)]

    # print out the dash mat for guessing
    word_length = len(random_word)
    guesser_container = ['-' for i in range(word_length)]
    # print(*guesser_container)
    # print()

    # set lives to 5
    

    lives = {}
    keys = list(d.keys())
    for key in keys:
        lives[key] = 3
    end = 0
    end_win = False
    lives_temp = copy.deepcopy(lives)
    while True:
        keys = list(d.keys())
        for key in keys:
            while True:
                print()
                print(*guesser_container)
                
                if lives[key] == 0:
                    break

                if d[key] >= 5 : 
                    print(key,'Currently you earned : ' , d[key]//5, 'coins')
                alphabet = input(key+' Enter your guess alphabet/word : ')
                
                # if the user only entered 1 letter
                if len(alphabet) == 1:
                    if alphabet in random_word:
                        # find the indexes that appear inside this random word
                        for i in range(word_length):
                            if alphabet == random_word[i]:
                                guesser_container[i] = alphabet
                    else:
                        print('Wrong guess ! Guess Again.')
                        lives[key]-=1
                        print('Remaining Lives : ', lives[key])
                        break
                else:
                    # when user wants to key in the whole word
                    if random_word == alphabet:
                        print('-------You Won ------')
                        d[key] +=1
                        print('The answer is : ', random_word)
                        print("Your Current Score is : ", d[key])
                        for i in range(3,0,-1):
                            print('Next question in',i+1,'seconds')
                            time.sleep(1)
                        end_win = True
                        break
                    else:
                        print('Wrong guess ! Guess Again.')
                        lives[key]-=1
                        print('Remaining Lives : ', lives[key])
                        break

                        
                
                # print(*guesser_container)
                # break when all the dash are filled up
                if '-' not in  guesser_container:
                    d[key] +=1
                    print('-------You Won ------')
                    print('The answer is : ', random_word)
                    print("Your Current Score is : ", d[key])
                    for i in range(3,0,-1):
                        print('Next question in',i+1,'seconds')
                        time.sleep(1)
                    end_win = True

                    break
            
            if lives[key] == 0:
                end += 1
                
                print("----You Lost No more Lives -----")
                # print('The answer is : ', random_word)
                print(key," Your Current Score is : ", d[key])
                print()
                d.pop(key)
                lives.pop(key)
                # for i in range(3,0,-1):
                #         print('Next Person continue in',i+1,'seconds')
                #         time.sleep(1)
                break
            if len(d) == 0:
                break
            if end_win == True:
                break
        # print(end,len(d))
        if len(d) == 0:
            print('The answer is : ', random_word)
            for i in range(3,0,-1):
                        print('Next question in',i+1,'seconds')
                        time.sleep(1)
            print('breaking loop .......')
            d = copy.deepcopy(temp)
            lives = copy.deepcopy(lives_temp)
            break
        if end_win == True:
                break
    