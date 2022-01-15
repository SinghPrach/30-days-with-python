vowels = 'aeiou'
my_string = 'Hi, my name is Prachi Singh'

# making it suitable for case-less comparison
my_string = my_string.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels, 0)

# count the number of vowels
for char in my_string:
    if char in count:
        count[char] += 1

print(count)
