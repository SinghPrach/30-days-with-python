num_list = []   #list of the numbers to be checked

# number of elements as input
terms = int(input("Enter total number of numbers to be checked= "))
print('Enter the numbers to be checked')
# iterating till the range
for i in range(terms):
    div = int(input('Enter: '))  # dividends

    num_list.append(div)  # adding the element

# Here we are checking divisibility by 12
result = list(filter(lambda x: (x % 12 == 0), num_list))

# display the result
print("Numbers divisible by 12 are", result)
