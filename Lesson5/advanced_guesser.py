import random
word_pool = []

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

    # set for 3 lives

    lives = 3
    while True:
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
        else:
            # when user wants to key in the whole word
            if random_word == alphabet:
                print('-------You Won ------')
                print('The answer is : ', random_word)
                break
                
        
        print(*guesser_container)
        # break when all the dash are filled up
        if '-' not in  guesser_container:
            print('-------You Won ------')
            print('The answer is : ', random_word)
            break
        if lives == 0:
            print("----You Lost No more Lives -----")
            print('The answer is : ', random_word)
            break