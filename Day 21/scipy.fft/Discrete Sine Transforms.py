from scipy.fft import dst, idst
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

------------------------------------------------

dst(dst(x, type=2, norm='ortho'), type=3, norm='ortho')
array([ 1. ,  2. ,  1. , -1. ,  1.5])

------------------------------------------------

dst(dst(x, type=2), type=3)
array([ 10.,  20.,  10., -10.,  15.])

------------------------------------------------

idst(dst(x, type=2), type=2)
array([ 1. ,  2. ,  1. , -1. ,  1.5])

------------------------------------------------

dst(dst(x, type=1, norm='ortho'), type=1, norm='ortho')
array([ 1. ,  2. ,  1. , -1. ,  1.5])
 # scaling factor 2*(N+1) = 12
dst(dst(x, type=1), type=1)
array([ 12.,  24.,  12., -12.,  18.])
 # no scaling factor
idst(dst(x, type=1), type=1)
array([ 1. ,  2. ,  1. , -1. ,  1.5])

------------------------------------------------

dst(dst(x, type=4, norm='ortho'), type=4, norm='ortho')
array([ 1. ,  2. ,  1. , -1. ,  1.5])
 # scaling factor 2*N = 10
dst(dst(x, type=4), type=4)
array([ 10.,  20.,  10., -10.,  15.])
 # no scaling factor
idst(dst(x, type=4), type=4)
array([ 1. ,  2. ,  1. , -1. ,  1.5])
