# Making a simple calculator


def add(x, y):      # addition
    z = x + y
    return z


def sub(x, y):      # subtraction
    z = x - y
    return z


def mult(x, y):     # multiplication
    z = x * y
    return z


def div(x, y):      # division
    z = x / y
    return z


print('This calculator performs Addition, Subtraction, Multiplication, and Division')
print('For addition, enter 1')
print('For subtraction, enter 2')
print('For multiplication, enter 3')
print('For division, enter 4')

while True:
    operation = int(input('Enter your choice: '))
    if operation in (1, 2, 3, 4):
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        if operation == 1:
            print(num1, "+", num2, "=", add(num1, num2))
        elif operation ==2:
            print(num1, "-", num2, "=", sub(num1, num2))
        elif operation == 3:
            print(num1, "*", num2, "=", mult(num1, num2))
        elif operation == 4:
            print(num1, "/", num2, "=", div(num1, num2))
        next_calculation = input("Do you want to do more calculation? (yes/no) ")
        if next_calculation == "no":
            break
    else:
        print('Please provide valid choice')
