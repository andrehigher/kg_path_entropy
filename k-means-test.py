from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0], [8, 8], [5, 5], [6, 5], [6, 0]])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
print kmeans.labels_
print kmeans.predict([[0, 0], [8, 4], [4, 4]])
print kmeans.cluster_centers_

# import numpy as np # I want to check my solution with numpy

# x = [0, 0, 0, 0, 0]
# y = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
# z = [[0], [1], [1], [1], [0]]
# mx = np.matrix(x)
# my = np.matrix(y)
# mz = np.matrix(z)
# result = mx * my
# print result
# print result * mz
