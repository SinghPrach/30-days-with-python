# A B-spline is an approximation of a continuous function over a finite- domain in terms of B-spline coefficients and knot points.

import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt


image = misc.face(gray=True).astype(np.float32)
derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
ck = signal.cspline2d(image, 8.0)
deriv = (signal.sepfir2d(ck, derfilt, [1]) +
         signal.sepfir2d(ck, [1], derfilt))

plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()

# For output of spline edge filter
import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt


image = misc.face(gray=True).astype(np.float32)
derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
ck = signal.cspline2d(image, 8.0)
deriv = (signal.sepfir2d(ck, derfilt, [1]) +
         signal.sepfir2d(ck, [1], derfilt))

plt.figure()
plt.imshow(deriv)
plt.gray()
plt.title('Output of spline edge filter')
plt.show()
