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
import networkx as nx
edges_entropy = {}
G=nx.DiGraph()
G.add_edges_from([('A','B',{'relation':'test'})])
G.add_edges_from([('A','E',{'relation':'test'})])
G.add_edges_from([('A','F',{'relation':'test'})])
G.add_edges_from([('B','C',{'relation':'test'})])
G.add_edges_from([('B','D',{'relation':'test'})])
G.add_edges_from([('B','E',{'relation':'test'})])
print G.edges()
edges = G.edges()
vertex_random = 'A'
print 'Degree', G.degree(vertex_random)
print 'In degree', G.in_degree(vertex_random)
print 'Out degree', G.out_degree(vertex_random)
print 'Successors', G.successors(vertex_random)
# print G.adjacency_list()
# we check every vertex in the graph which is not connected with selected vertex
for seed in G.nodes():
    if seed != vertex_random:
        if seed not in G.successors(vertex_random):
            print(seed, ' is not a sucessor')
            prod = 1.0
            print 'Degree', G.degree(seed)
            for i in range(G.degree(seed)):
                prod = prod * ((len(edges)-G.degree(vertex_random)+(-i+1)+1)/float(len(edges)+(-i+1)+1))
            print('Probability to have a connection', 1 - prod)