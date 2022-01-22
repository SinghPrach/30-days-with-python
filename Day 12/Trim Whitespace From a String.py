#Using strip()
my_string = ' I love my India '

print(my_string.strip())

#Using strip()
my_string = ' \nI love my India '

print(my_string.strip(' '))

#Using regular expression
import re

my_string = ' Hello World '
output = re.sub(r'^\s+|\s+$', '', my_string)

print(output)
