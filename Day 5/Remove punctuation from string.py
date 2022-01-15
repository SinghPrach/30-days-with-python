# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_string = "Hello!!!, he said ---and went."

# removing punctuation from the string
no_punct = ''
for char in my_string:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)
