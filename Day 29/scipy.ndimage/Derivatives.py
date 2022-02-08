'''For second derivative'''
derivative2(input, axis, output, mode, cval, *extra_arguments, **extra_keywords)

''' To demonstrate the use of the extra_arguments argument'''
def d2(input, axis, output, mode, cval, weights):
...     return correlate1d(input, weights, axis, output, mode, cval, 0,)
...
a = np.zeros((5, 5))
a[2, 2] = 1
generic_laplace(a, d2, extra_arguments = ([1, -2, 1],))
'''array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  1., -4.,  1.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])'''
# or
generic_laplace(a, d2, extra_keywords = {'weights': [1, -2, 1]})
'''array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  1., -4.,  1.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])'''

-----------------------------------------------------
# For first derivative
derivative(input, axis, output, mode, cval, *extra_arguments, **extra_keywords)
