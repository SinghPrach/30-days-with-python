''' A Voronoi diagram is a subdivision of the space into the nearest neighborhoods of a given set of points. '''

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
                   [2, 0], [2, 1], [2, 2]])
tree = KDTree(points)
tree.query([0.1, 0.1])
x = np.linspace(-0.5, 2.5, 31)
y = np.linspace(-0.5, 2.5, 33)
xx, yy = np.meshgrid(x, y)
xy = np.c_[xx.ravel(), yy.ravel()]

dx_half, dy_half = np.diff(x[:2])[0] / 2., np.diff(y[:2])[0] / 2.
x_edges = np.concatenate((x - dx_half, [x[-1] + dx_half]))
y_edges = np.concatenate((y - dy_half, [y[-1] + dy_half]))
plt.pcolormesh(x_edges, y_edges, tree.query(xy)[1].reshape(33, 31), shading='flat')
plt.plot(points[:,0], points[:,1], 'ko')
plt.show()
