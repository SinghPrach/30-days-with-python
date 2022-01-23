#Using glob
import glob, os

os.chdir('directory_name')

for file in glob.glob("*.txt"):
    print(file)

#Using os
import os

for file in os.listdir('directory_name'):
    if file.endswith(".txt"):
        print(file)
        
#Using os.walk
import os

for root, dirs, files in os.walk('directory_name'):
    for file in files:
        if file.endswith(".txt"):
            print(file)
