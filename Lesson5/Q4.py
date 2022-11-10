word = input('Enter a word: ').lower()

# become a list of characters
word = list(word)

index_list = []
for i in range(len(word)):
    if word[i]== 'a':
        index_list.append(i)

print(*index_list)

