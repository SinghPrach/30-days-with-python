#Using zip 
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c','d']

for i, j in zip(list_1, list_2):
    print(i, j)

#Using itertools
import itertools

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c','d']

# loop until the short loop stops
for i,j in itertools.izip(list_1,list_2):
    print i,j

print("\n")

# loop until the longer list stops
for i,j in itertools.izip_longest(list_1,list_2):
    print i,j
