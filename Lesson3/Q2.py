words = []
while True:
    word = input('Enter a word: ')
    if word == 'end':
        break
    words.append(word)
print('Ans :',*words)
