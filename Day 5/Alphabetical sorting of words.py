my_string = 'Hi, my name is Prachi Singh'

# breaking the string into a list of words
words = [word.lower() for word in my_string.split()]

# sorting the list
words.sort()

# displaying the sorted words

print('The alphabetically sorted words are:')
for word in words:
    print(word)
