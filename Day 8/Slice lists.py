#Getting all the items of a list
my_list = [1, 2, 'Prachi', 'Singh', 5, 6, 7]

print(my_list[:])

#Getting list from a specific position
my_list = [1, 2, 'Prachi', 'Singh', 5, 6, 7]

print(my_list[2:])
#Output: ['Prachi', 'Singh', 5, 6, 7]

#Getting list before a specific position
my_list = [1, 2, 'Prachi', 'Singh', 5, 6, 7]

print(my_list[:2])
#Output:[1, 2]

#Getting list between two specific positions
my_list = [1, 2, 'Prachi', 'Singh', 5, 6, 7]

print(my_list[2:4])

#Getting list at specified intervals of positions
my_list = [1, 2, 'Prachi', 'Singh', 5, 6, 7]

print(my_list[::2])
#Output: [1, 'Prachi', 5, 7]

my_list = [1, 2, 'Prachi', 'Singh', 5, 6, 7]

print(my_list[1:4:2])
#Output: [2, 'Singh']
