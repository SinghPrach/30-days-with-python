#Using a while loop
base = 4
exponent = 3

result = 1

while exponent != 0:
    result *= base
    exponent -= 1

print('Answer = ' + str(result))

#Using a for loop
base = 4
exponent = 3

result = 1
for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))

#Using pow()
base = 4
exponent = 3

result = pow(base, exponent)

print("Answer = " + str(result))


