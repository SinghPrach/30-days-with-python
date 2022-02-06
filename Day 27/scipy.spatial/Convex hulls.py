'''A convex hull is the smallest convex object containing all points in a given point set.'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

rng = np.random.default_rng()
points = rng.random((30, 2))   # 30 random points in 2-D
hull = ConvexHull(points)


plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()
