#Using glob
import glob, os

os.chdir('directory_name')

for file in glob.glob("*.txt"):
    print(file)

#Using os
