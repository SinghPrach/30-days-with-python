import scipy.io as sio
import numpy as np

#Save a mat file
vect = np.arange(10)
sio.savemat('array.mat', {'vect':vect})

#Now Load the File
mat_file_content = sio.loadmat(‘array.mat’)
print mat_file_content

# Different Way
import scipy.io as sio
mat_file_content = sio.whosmat(‘array.mat’)
print mat_file_content
