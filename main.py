#!/usr/bin/env python
import sys
import operator
import networkx as nx
from util import Util
from graph import Graph
from random import choice
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
    L = 3
    NUMBER_OF_TESTS = 20

    MMR = 0.0
    for i in range(0,NUMBER_OF_TESTS):
        
        v1 = choice(g.nodes())
        v2 = choice(g.neighbors(v1))
        edge_to_be_predicted = graph.get_relation(v1, v2)
        print v1, v2, graph.get_relation(v1, v2)
        g.remove_edge(v1,v2)

        # Generate distribution over paths between v1 and v2 at most L
        distribution = graph.generate_distribution(v1, v2, L)

        # Walk over found paths and generate dictionary from ocurrence edges between v1 and v2
        distribution_path = graph.generate_edges_between_paths(distribution)

        # Get both distribution calculated above and 
        final_distribution = graph.generate_final_distribution(distribution, distribution_path)

        # Get domain from most outgoing edges from source
        domain = graph.get_domain(v1)

        # How to use test and valid datasets ???
        # graph.clear()
        # util.read_file('dataset/fb15k/test.txt', graph)

        final_distribution_sorted = sorted(final_distribution.items(), key=operator.itemgetter(1), reverse=True)
        print final_distribution_sorted

        count = 0.0
        for relation, probability in final_distribution_sorted:
            print 'Predicting', relation
            if relation == edge_to_be_predicted:
                count += 1.0
                break;
            if relation == None and probability > 0.92:
                count += 1.0
            elif relation != None:
                count += 1.0
        print 'Current MMR', MMR
        print 'count', count
        if count == 0:
            count = 1
        MMR += (1.0/count)
        print 'MMR updated', MMR
        g.add_edge(v1, v2,{'relation':edge_to_be_predicted})
        graph.set_relation(v1, v2, edge_to_be_predicted)

    print 'Final MMR: ', (MMR/NUMBER_OF_TESTS)