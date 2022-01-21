#Check for float
def check_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


value = input('Enter any value you want to check: ')
print(check_float(value))

#Check for int
def check_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


value = input('Enter any value you want to check: ')
print(check_int(value))
