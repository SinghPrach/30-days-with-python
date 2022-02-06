from scipy.spatial import Delaunay
import numpy as np

points = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [1, 1]])
tri = Delaunay(points)
print(np.unique(tri.simplices.ravel()))

print(tri.coplanar)
