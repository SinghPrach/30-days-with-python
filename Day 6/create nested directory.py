# Using pathlib.Path.mkdir
from pathlib import Path
Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)

# Using os.makedirs
import os

os.makedirs("/root/dirA/dirB")

# Using distutils.dir_util
import distutils.dir_util

distutils.dir_util.mkpath("/root/dirA/dirB")

# Raising an exception if directory already exists
import os

try:
    os.makedirs("/dirA/dirB")
except FileExistsError:
    print("File already exists")
