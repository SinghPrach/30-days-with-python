# Using list comprehension
my_list = [[1], [2, 'Prachi'], ['Singh', 5, 6, 7]]

flatten_list = [num for sublist in my_list for num in sublist]
print(flatten_list)

# Using for loop
my_list = [[1], [2, 'Prachi'], ['Singh', 5, 6, 7]]

flatten_list = []
for sublist in my_list:
    for num in sublist:
        flatten_list.append(num)

print(flatten_list)

# Using itertools
import itertools

my_list = [[1], [2, 'Prachi'], ['Singh', 5, 6, 7]]

flat_list = list(itertools.chain(*my_list))
print(flat_list)

Using sum()
my_list = [[1], [2, 'Prachi'], ['Singh', 5, 6, 7]]

flatten_list = sum(my_list, [])
print(flatten_list)

#Using lambda and reduce()
from functools import reduce

my_list = [[1], [2, 'Prachi'], ['Singh', 5, 6, 7]]

print(reduce(lambda x, y: x + y, my_list))

