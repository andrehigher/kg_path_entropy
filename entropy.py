#!/usr/bin/env python
import operator
import math
import sys
import networkx as nx
import matplotlib.pyplot as plt

def calculate_entropy(G, source, target):
    prod = 1.0
    for i in range(1, G.degree(target)+1):
        prod = prod * (float(num_edges-G.degree(source)-i+1)/float(num_edges-i+1))
    return -math.log(1 - prod, 2)

def calculate_entropy_beta(G, source, target, edges):
    prod = 1.0
    for i in range(1, G.degree(target)+1):
        prod = prod * (float(edges-G.degree(source)-i+1)/float(edges-i+1))
    return -math.log(1 - prod, 2)

def walk(G, max_length, node_start, current_length, nodes_visited = []):
    print max_length, node_start, current_length, nodes_visited
    if current_length > max_length:
        return nodes_visited
    for target in G.neighbors(node_start):
        if target not in nodes_visited:
            nodes_visited.append(target)
            walk(G, max_length, target, current_length+1, nodes_visited)
            return nodes_visited

if __name__ == "__main__":
    # Create the graph
    G=nx.Graph()
    G.add_edge(0,1)
    G.add_edge(0,7)
    G.add_edge(0,4)
    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(4,5)
    G.add_edge(5,6)
    G.add_edge(5,3)
    G.add_edge(7,8)
    G.add_edge(8,9)
    num_edges = len(G.edges())

    # # Calculate every entropy edge in the graph
    # for edge in G.edges():
    #     print edge, calculate_entropy(G, edge[0], edge[1])

    # for node in G.nodes():
    #     paths = nx.all_simple_paths(G, 0, node, cutoff=3)
    #     print(list(paths))

    paths = nx.all_simple_paths(G, 0, 3, cutoff=3)
    path_entropy_all = 0
    for path in list(paths):
        path_entropy = 0
        for i in range(0, len(path)-1):
            path_entropy = path_entropy + calculate_entropy(G, path[i], path[i+1])
        path_entropy_all = path_entropy_all + path_entropy*(1/(float((len(path)-1)-1)))
    print 'entropy path 0 -> 3 - ', path_entropy_all-calculate_entropy(G, 0, 3)

    paths = nx.all_simple_paths(G, 0, 2, cutoff=3)
    path_entropy_all = 0
    for path in list(paths):
        path_entropy = 0
        for i in range(0, len(path)-1):
            path_entropy = path_entropy + calculate_entropy(G, path[i], path[i+1])
        path_entropy_all = path_entropy_all + path_entropy*(1/(float((len(path)-1)-1)))
    print 'entropy path 0 -> 2 - ', path_entropy_all-calculate_entropy(G, 0, 2)
        