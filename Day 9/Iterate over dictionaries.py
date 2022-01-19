#Using items()
my_dict = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in my_dict.items():
    print(key, value)

#Without using items()
my_dict = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in my_dict:
    print(key, my_dict[key])
    
#Using iteritems()
my_dict = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in my_dict.iteritems():
    print(key, value)
    
#Using keys() and values()
my_dict = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)
