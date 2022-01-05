num = int(input('Enter any number= '))  # enter any natural number
n = len(str(num))  # this gives the number of digits in any number
sum = 0  # initialize the sum of the digits of the number

temp = num
while temp > 0:
    digit = temp % 10
    sum += pow(digit, n)
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
