import numpy as np
word_list = np.asarray(word_list)
word_list.dtype   # these are unicode characters in Python 3
word_list.sort()  # sort for quick searching later
word_bytes = np.ndarray((word_list.size, word_list.itemsize),
                        dtype='uint8',
                        buffer=word_list.data)
# each unicode character is four bytes long. We only need first byte
# we know that there are three characters in each word
word_bytes = word_bytes[:, ::word_list.itemsize//3]
word_bytes.shape

# Using Hamming distance between each point to determine which pairs of words are connected
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
hamming_dist = pdist(word_bytes, metric='hamming')
# there are three characters in each word
graph = csr_matrix(squareform(hamming_dist < 1.5 / 3))
i1 = word_list.searchsorted('ape')
i2 = word_list.searchsorted('man')
word_list[i1]
# 'ape'
word_list[i2]
# 'man'
