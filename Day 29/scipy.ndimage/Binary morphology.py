from scipy.ndimage import generate_binary_structure
generate_binary_structure(2, 1)
'''array([[False,  True, False],
       [ True,  True,  True],
       [False,  True, False]], dtype=bool)'''
generate_binary_structure(2, 2)
'''array([[ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True]], dtype=bool)'''
