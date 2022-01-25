#Opening Files
f = open("name of file.txt")    # open file in current directory
f = open("C:/Python38/README.txt")  # specifying full path

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

#Closing Files
f = open("name of file.txt", encoding = 'utf-8')
# perform file operations
f.close()

try:
   f = open("name of file.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
    
#Writing to Files
with open("name of file.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   
#Reading Files
f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

f.read(4)    # read the next 4 data
' is '

f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'
f.read()  # further reading returns empty sting
''

f.readlines()
['This is my first file\n', 'This file\n', 'contains three lines\n']

