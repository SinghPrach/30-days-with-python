# pyramid of '*' signs
def pyramid_stars(num):
    for i in range(num):
        for j in range(i + 1):
            print("* ", end="")
        print("\n")


num_rows = int(input('Enter the number of rows you want to print: '))
pyramid_stars(num_rows)

# pyramid of numbers
def pyramid_numbers(num):
    for i in range(num):
        for j in range(i + 1):
            print(j+1, end='')
        print("\n")


num_rows = int(input('Enter the number of rows you want to print: '))
pyramid_numbers(num_rows)

# pyramid of alphabets
num_rows = int(input('Enter the number of rows you want to print: '))
ascii_value = 65

for i in range(num_rows):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=' ')

    ascii_value += 1
    print("\n")

# Floyd's triangle
num_rows = int(input('Enter the number of rows you want to print: '))
number = 1

for i in range(1, num_rows+1):
    for j in range(1, i+1):
        print(number, end=' ')
        number += 1
    print()
