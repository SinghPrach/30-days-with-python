from scipy.ndimage import correlate
import numpy as np

correlate(np.arange(10), [1, 2.5])
# ([ 0,  2,  6,  9, 13, 16, 20, 23, 27, 30])
correlate(np.arange(10), [1, 2.5], output=np.float64)
# ([  0. ,   2.5,   6. ,   9.5,  13. ,  16.5,  20. ,  23.5,  27. ,  30.5])
