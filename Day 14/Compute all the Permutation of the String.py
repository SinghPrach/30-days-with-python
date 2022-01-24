# Using recursion
def get_permutation(string, i=0):
    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]

        get_permutation(words, i + 1)


my_string = input('Enter any string: ')
print(get_permutation(my_string))

#Using itertools 
from itertools import permutations

my_string = input('Enter any string: ')
permutation_words = [''.join(p) for p in permutations(my_string)]

print(permutation_words)
