#Get Current Directory
import os

os.getcwd()
'C:\\Program Files\\PyScripter'

os.getcwdb()
b'C:\\Program Files\\PyScripter'

#Changing Directory
os.chdir('C:\\Python33')

print(os.getcwd())
C:\Python33
  
#Making a New Directory
os.mkdir('test')

os.listdir()
['test']

#Renaming a Directory or a File
os.listdir()
['test']

os.rename('test','new_one')

os.listdir()
['new_one']

#Removing Directory or File
os.listdir()
['new_one', 'old.txt']

os.remove('old.txt')
os.listdir()
['new_one']

os.rmdir('new_one')
os.listdir()
[]
