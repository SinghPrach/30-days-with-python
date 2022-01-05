def armstrong(num):
    n = len(str(num))
    sum = 0  # initialize the sum of the digits of the number
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += pow(digit, n)
        temp //= 10
    if num == sum:
        a = num
        print(a)


x = int(input('Enter the lower limit of the interval= '))
y = int(input('Enter the upper limit of the interval= '))

for i in range(x,y+1):
    z = armstrong(i)
