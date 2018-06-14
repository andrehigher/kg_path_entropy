""" A Python Class
A simple Python graph class to do essential operations into graph.
"""
import operator
import math
from random import choice
import networkx as nx

class Graph():

    def __init__(self, graph):
        """ Initializes util object.
        """
        self.__graph = graph

    def set_graph(self, graph):
        """ A method to set graph.
        """
        self.__graph = graph

    def get_graph(self):
        """ A method to get graph.
        """
        return self.__graph

    def calculate_entropy(self, source, target):
        """ Calculates the entropy from source and target.
        """
        prod = 1.0
        for i in range(1, self.__graph.degree(target)+1):
            prod = prod * (float(self.__graph.number_of_edges()-self.__graph.degree(source)-i+1)/float(self.__graph.number_of_edges()-i+1))
        return -math.log(1 - prod, 2)

    def calculate_common_neighbors(self, source, target):
        """ Calculates the common neighbors from source and target.
        """
        return sorted(nx.common_neighbors(self.__graph, source, target))

    def calculate_resource_allocation(self, source, target):
        """ Calculates the common neighbors from source and target.
        """
        return nx.resource_allocation_index(self.__graph, [(source, target)])

    def random_walk(self):
        """ A method to get started a random walk into graph
         selecting a node from random.
        """
        print 'Number of nodes', self.__graph.number_of_nodes()
        print 'Number of edges', self.__graph.number_of_edges()

        # Get a node randomly
        # Probability to get this first node is 1/N
        seed = choice(self.__graph.nodes())
        print 'Selected a node randomly', seed
        print 'Degree', self.__graph.degree(seed)
        print 'In degree', self.__graph.in_degree(seed)
        print 'Out degree', self.__graph.out_degree(seed)
        print 'Successors', self.__graph.successors(seed)
        num_edges = len(self.__graph.edges())
        prob_vertex = {}
        entropy_vertex = {}
        for possibility in self.__graph.nodes():
            if possibility != seed:
                if possibility not in self.__graph.successors(seed):
                    prod = 1.0
                    for i in range(self.__graph.degree(possibility)):
                        prod = prod * ((num_edges-self.__graph.degree(seed)+(-i+1)+1)/float(num_edges+(-i+1)+1))
                    prob_vertex[possibility] = 1 - prod
                    entropy_vertex[possibility] = -math.log(1 - prod)
        prob_vertex = sorted(prob_vertex.items(), key=operator.itemgetter(1))
        entropy_vertex = sorted(entropy_vertex.items(), key=operator.itemgetter(1))
        print entropy_vertex
        print seed
        # Print edges with relation
        # print DG.edges(data='relation')

    def entropy(self, source, target):
        """ A method to get started entropy calculation into graph
         selecting a node.
        """
        print('source:', source, 'target:', target, 'entropy:', self.calculate_entropy(source, target))

    def predict_facts(self, source, target, length):
        """ A method to predict facts based on shannon entropy.
        """
        print(source, target)
        print 'Selected a node', source
        print 'Source Degree', self.__graph.degree(source)
        print 'Neighbors', self.__graph.neighbors(source)
        print 'Target Degree', self.__graph.degree(target)
        print 'Neighbors', self.__graph.neighbors(target)

        
        # print(sorted(nx.all_neighbors(self.__graph, source)))
        print(len(self.__graph.edges()))
        # print(self.__graph.edges())
        count = 0.0
        for edge in self.__graph.edges():
            if edge[0] == 'teamplayssport' or edge[1] == 'teamplayssport':
                count = count + 1
            # print(edge)
        # print 'In degree', self.__graph.in_degree(source)
        # print 'Out degree', self.__graph.out_degree(source)
        # print 'Successors', self.__graph.successors(source)
        # print(sorted(nx.common_neighbors(self.__graph, source, target)))
        print(count)
        print(count/(len(self.__graph.edges())))
