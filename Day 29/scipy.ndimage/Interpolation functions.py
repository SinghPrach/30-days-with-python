a = np.arange(12).reshape(4,3).astype(np.float64)
def shift_func(output_coordinates):
...     return (output_coordinates[0] - 0.5, output_coordinates[1] - 0.5)
...
from scipy.ndimage import geometric_transform
geometric_transform(a, shift_func)
'''array([[ 0.    ,  0.    ,  0.    ],
       [ 0.    ,  1.3625,  2.7375],
       [ 0.    ,  4.8125,  6.1875],
       [ 0.    ,  8.2625,  9.6375]])'''
