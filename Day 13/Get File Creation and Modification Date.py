#Using os
import os.path
import pathlib
import time

file = pathlib.Path('ex3.py')  # ex 3 is the file name
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))

#Using stat() method
import datetime
import pathlib

fname = pathlib.Path('ex3.py')  # ex 3 is the file name
print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))
