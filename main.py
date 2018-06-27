#!/usr/bin/env python
import sys
import operator
import networkx as nx
from util import Util
from graph import Graph
from random import choice
from collections import defaultdict
import timeit

if __name__ == "__main__":
    start = timeit.default_timer()
    # print sys.argv
    DG = nx.Graph()
    util = Util()
    graph = Graph(DG)
    # util.read_file('dataset/fb15k/train.txt', graph)

    util.read_file('dataset/wn18/train.txt', graph)
    # util.read_file('dataset/nell/nell_cleaned.txt', graph)
           
    g = graph.get_graph()
    L = 5
    NUMBER_OF_TESTS = 10

    MMR = 0.0
    HITS_1 = 0.0
    HITS_3 = 0.0
    HITS_5 = 0.0
    HITS_10 = 0.0
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
            count = 20.0
        else:
            MMR += (1.0/count)
        print 'MMR updated', MMR
        if count == 1:
            HITS_1 += 1
        if count <= 3:
            HITS_3 += 1
        if count <= 5:
            HITS_5 += 1
        if count <= 10:
            HITS_10 += 1

        g.add_edge(v1, v2,{'relation':edge_to_be_predicted})
        graph.set_relation(v1, v2, edge_to_be_predicted)

    stop = timeit.default_timer()
    print 'Final MMR: ', (MMR/NUMBER_OF_TESTS)
    print 'Final HITS@1', (HITS_1/NUMBER_OF_TESTS)
    print 'Final HITS@3', (HITS_3/NUMBER_OF_TESTS)
    print 'Final HITS@5', (HITS_5/NUMBER_OF_TESTS)
    print 'Final HITS@10', (HITS_10/NUMBER_OF_TESTS)
    print 'Final Time:', stop - start
