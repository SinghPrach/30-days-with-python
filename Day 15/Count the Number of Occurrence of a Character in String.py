#Using for loop
count = 0

my_string = input('Enter any string: ')
my_char = input('Enter any character: ')

for i in my_string:
    if i == my_char:
        count += 1

print('The number of occurrence is', count)

#Using method count()
my_string = input('Enter any string: ')
my_char = input('Enter any character: ')

print('The number of occurrence is', my_string.count(my_char))
