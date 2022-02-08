import numpy as np
footprint = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
print(footprint)

''' correlation of a 1-D array with a filter of length 3 consisting of ones'''
from scipy.ndimage import correlate1d
a = [0, 0, 0, 1, 0, 0, 0]
correlate1d(a, [1, 1, 1])
# array([0, 0, 1, 1, 1, 0, 0])

''' calculation of backward and forward differences'''
a = [0, 0, 1, 1, 1, 0, 0]
correlate1d(a, [-1, 1])               # backward difference
# array([ 0,  0,  1,  0,  0, -1,  0])
correlate1d(a, [-1, 1], origin = -1)  # forward difference
# array([ 0,  1,  0,  0, -1,  0,  0])
correlate1d(a, [0, -1, 1])
# array([ 0,  1,  0,  0, -1,  0,  0])  # forward difference
