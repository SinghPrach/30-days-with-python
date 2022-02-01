# When N=2,correlate and/or convolve can be used to construct arbitrary image filters to perform actions such as blurring, enhancing, and edge-detection for an image.

import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
image = misc.face(gray=True)
w = np.zeros((50, 50))
w[0][0] = 1.0
w[49][25] = 1.0
image_new = signal.fftconvolve(image, w)
plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()

plt.figure()
plt.imshow(image_new)
plt.gray()
plt.title('Filtered image')
plt.show()

# We consider a Gaussian filter gaussian which is often used for blurring.

from scipy import signal, misc
import matplotlib.pyplot as plt
image = misc.ascent()
w = signal.windows.gaussian(51, 10.0)
image_new = signal.sepfir2d(image, w, w)
plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()
plt.figure()
plt.imshow(image_new)
plt.gray()
plt.title('Filtered image')
plt.show()
