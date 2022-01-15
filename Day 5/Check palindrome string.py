# Check if the string is palindrome

my_string = 'aIbohPhoBiA'

# make it suitable for case-less comparison
my_string = my_string.casefold()

# reverse the string
rev_string = reversed(my_string)

# check if the string is equal to its reverse
if list(my_string) == list(rev_string):
    print('The string is a palindrome.')
else:
    print('The string is not a palindrome.')
