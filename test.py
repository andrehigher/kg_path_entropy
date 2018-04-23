## CALCULUS OF PROBABILITY TO HAVE A LINK BETWEEN NODES
# m = 394804
# ka = 9
# kb = 114
# result = 1.0
# for i in range(kb):
#     result = (result * ((m-ka)-i+1))/(m-i+1)
#     print '(m-ka)-i+1)', ((m-ka)-i+1)
#     print '(m-i+1)', (m-i+1)
#     print 'result', result

# print result




## ADD ATTRIBUTES TO NODES AND EDGES
# import networkx as nx
# edges_entropy = {}
# G=nx.DiGraph()
# G.add_edges_from([('A','B',{'relation':'test'})])
# G.add_edges_from([('A','E',{'relation':'test'})])
# G.add_edges_from([('A','F',{'relation':'test'})])
# G.add_edges_from([('B','C',{'relation':'test'})])
# G.add_edges_from([('B','D',{'relation':'test'})])
# G.add_edges_from([('B','E',{'relation':'test'})])
# print G.edges()
# edges = G.edges()
# vertex_random = 'A'
# print 'Degree', G.degree(vertex_random)
# print 'In degree', G.in_degree(vertex_random)
# print 'Out degree', G.out_degree(vertex_random)
# print 'Successors', G.successors(vertex_random)
# # print G.adjacency_list()
# # we check every vertex in the graph which is not connected with selected vertex
# for seed in G.nodes():
#     if seed != vertex_random:
#         if seed not in G.successors(vertex_random):
#             print(seed, ' is not a sucessor')
#             prod = 1.0
#             print 'Degree', G.degree(seed)
#             for i in range(G.degree(seed)):
#                 prod = prod * ((len(edges)-G.degree(vertex_random)+(-i+1)+1)/float(len(edges)+(-i+1)+1))
#             print('Probability to have a connection', 1 - prod)



# MACHINE LEARNING LEARNING
from sklearn import datasets, linear_model, svm, neighbors, cluster
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
digits = datasets.load_digits()
diabetes = datasets.load_diabetes()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

### KNN
# knn = neighbors.KNeighborsClassifier(n_neighbors=1)
# knn.fit(X, y)
# print(knn.predict([[3, 5, 4, 2]]))
# print(iris.target_names[knn.predict([[3, 5, 4, 2]])])

### K-MEANS
# k_means = cluster.KMeans(n_clusters=3)
# k_means.fit(X)
# print(k_means.predict(X))

### LINEAR REGRESSION
linear = linear_model.LinearRegression()
print(linear.fit(X_train, y_train))
print(linear.score(X_train, y_train))
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
#Predict Output
print(linear.predict(X_test))
