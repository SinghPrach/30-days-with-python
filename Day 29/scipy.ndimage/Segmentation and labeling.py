# Segmentation is the process of separating objects of interest from the background.

a = np.array([[1,2,2,1,1,0],
...               [0,2,3,1,2,0],
...               [1,1,1,3,3,2],
...               [1,1,1,1,2,1]])
np.where(a > 1, 1, 0)
'''array([[0, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 0],
       [0, 0, 0, 1, 1, 1],
       [0, 0, 0, 0, 1, 0]])'''
----------------------------------------------------------------------
'''In 2D using a 4-connected structuring element'''

a = np.array([[0,1,1,0,0,0],[0,1,1,0,1,0],[0,0,0,1,1,1],[0,0,0,0,1,0]])
s = [[0, 1, 0], [1,1,1], [0,1,0]]
from scipy.ndimage import label
label(a, s)
'''(array([[0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 2, 0],
        [0, 0, 0, 2, 2, 2],
        [0, 0, 0, 0, 2, 0]]), 2)'''
----------------------------------------------------------------------
'''The watershed_ift function applies a watershed from markers algorithm, using Image Foresting Transform.'''
input = np.array([[0, 0, 0, 0, 0, 0, 0],
...                   [0, 1, 1, 1, 1, 1, 0],
...                   [0, 1, 0, 0, 0, 1, 0],
...                   [0, 1, 0, 0, 0, 1, 0],
...                   [0, 1, 0, 0, 0, 1, 0],
...                   [0, 1, 1, 1, 1, 1, 0],
...                   [0, 0, 0, 0, 0, 0, 0]], np.uint8)
markers = np.array([[1, 0, 0, 0, 0, 0, 0],
...                     [0, 0, 0, 0, 0, 0, 0],
...                     [0, 0, 0, 0, 0, 0, 0],
...                     [0, 0, 0, 2, 0, 0, 0],
...                     [0, 0, 0, 0, 0, 0, 0],
...                     [0, 0, 0, 0, 0, 0, 0],
...                     [0, 0, 0, 0, 0, 0, 0]], np.int8)
from scipy.ndimage import watershed_ift
watershed_ift(input, markers)
'''array([[1, 1, 1, 1, 1, 1, 1],
       [1, 1, 2, 2, 2, 1, 1],
       [1, 2, 2, 2, 2, 2, 1],
       [1, 2, 2, 2, 2, 2, 1],
       [1, 2, 2, 2, 2, 2, 1],
       [1, 1, 2, 2, 2, 1, 1],
       [1, 1, 1, 1, 1, 1, 1]], dtype=int8)'''