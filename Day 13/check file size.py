#Using os module
import os

file_size = os.stat('data.txt')   #data.txt is the name of the file
print(file_size.st_size)

#Using pathlib module
from pathlib import Path

file = Path('data.txt')   #data.txt is the name of the file
print(file.stat().st_size)
