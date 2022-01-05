num = float(input('Enter any year= '))  # enter the year to be checked
t = num % 100  # last two digits of the year
a = t % 4  # remainder when divided by 4
if a == 0:
    print('{0} is a leap year'.format(num))
else:
    print('{0} is not a leap year'.format(num))
