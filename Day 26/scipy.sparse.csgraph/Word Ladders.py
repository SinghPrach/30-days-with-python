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
