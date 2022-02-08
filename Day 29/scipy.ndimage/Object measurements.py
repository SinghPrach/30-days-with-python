a = np.array([[0,1,1,0,0,0],[0,1,1,0,1,0],[0,0,0,1,1,1],[0,0,0,0,1,0]])
l, n = label(a)
from scipy.ndimage import find_objects
f = find_objects(l)
a[f[0]]
'''array([[1, 1],
       [1, 1]])'''
a[f[1]]
'''array([[0, 1, 0],
       [1, 1, 1],
       [0, 1, 0]])'''
