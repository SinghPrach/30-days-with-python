#Using os module
import os

# file name with extension
file_name = os.path.basename('/root/file.ext')

# file name without extension
print(os.path.splitext(file_name)[0])

#Using Path module
from pathlib import Path

print(Path('/root/file.ext').stem)
