#Using splitext()
import os
file_details = os.path.splitext('/path/filename.ext')
print(file_details)
print(file_details[1])

#Using pathlib
import pathlib
print(pathlib.Path('/path/filename.ext').suffix)
