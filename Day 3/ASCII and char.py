# Converting char to ASCII and vice-versa

char = input('Enter any character= ')
ASCII_char = ord(char)  # Built-in function to find ASCII of a character
ASCII = int(input('Enter any ASCII value= '))
char_ASCII = chr(ASCII)     # Built-in function to find a character from an ASCII
print('The ASCII value of', char, 'is', ASCII_char)
print('The character corresponding to the', ASCII, 'is', char_ASCII)
