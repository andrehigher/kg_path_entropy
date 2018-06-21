#!/usr/bin/env python
import sys
import networkx as nx
from util import Util
from graph import Graph
from collections import defaultdict

if __name__ == "__main__":
    # print sys.argv
    DG = nx.Graph()
    util = Util()
    graph = Graph(DG)
    util.read_file('dataset/fb15k/train.txt', graph)
    # util.read_file('dataset/wn18/train.txt', graph)
    # util.read_file('dataset/nell/nell_cleaned.txt', graph)
        
    g = graph.get_graph()
    # EDGE TO BE PREDICTED 
    
    # FB15
    # V1 /m/01bpn - Bertrand Russell
    # V2 /m/02_xgp2 - Doctorate

    # WN18
    # V1 06845599
    # V2 02716866

    # L = 3
    v1 = '/m/01bpn'
    v2 = '/m/02_xgp2'
    L = 3

    # Generate distribution over paths between v1 and v2 at most L
    distribution = graph.generate_distribution(v1, v2, L)
    print(distribution)
    print(sum(distribution.values()))

    # Walk over found paths and generate dictionary from ocurrence edges between v1 and v2
    distribution = graph.generate_edges_between_paths(distribution)
    print(distribution)

    # graph.random_walk()
    # graph.predict_facts('tom_brady', 'new_england_patriots', 4)