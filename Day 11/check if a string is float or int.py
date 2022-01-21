def check_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


value = input('Enter any value you want to check: ')
print(check_float(value))
