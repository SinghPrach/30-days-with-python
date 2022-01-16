# Using readlines()
with open('data.txt') as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)

# Using loop
with open('data_file.txt') as f:
    content_list = [line for line in f]

print(content_list)

# removing the characters
with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]

print(content_list)
