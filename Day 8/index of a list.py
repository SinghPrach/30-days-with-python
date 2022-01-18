# Using enumerate()
my_list = [2, 27, 35, 11]

for index, value in enumerate(my_list):
    print(index, value)
    
# Index start different
my_list = [2, 27, 35, 11]

for index, value in enumerate(my_list, start=1):    # can be started from 1, 2, 3, any number
    print(index, value)
    
# Without using enumerate()
my_list = [2, 27, 35, 11]

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)
    
    
