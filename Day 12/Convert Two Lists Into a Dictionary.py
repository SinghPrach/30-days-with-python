#Using zip and dict methods
months_number = [1, 2, 3]
months_name = ['January', 'February', 'March']

dictionary = dict(zip(months_number,months_name))
print(dictionary)

#Using list comprehension
months_number = [1, 2, 3]
months_name = ['January', 'February', 'March']

dictionary = {k: v for k, v in zip(months_number,months_name)}
print(dictionary)
