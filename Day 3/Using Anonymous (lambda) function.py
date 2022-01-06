#Lamba functions' syntax: lambda arguments: expression
# Finding powers of any numbers using anonymous (Lambda) function

x = int(input('Enter any number= '))
y = int(input('Enter the number of terms= '))

result = list(map(lambda z: x ** z, range(y)))

for i in range(1, y):
    print(x, 'raised to power', i, 'is', result[i])

print('For printing values from 0')

for i in range(y):
    print(x, 'raised to power', i, 'is', result[i])
