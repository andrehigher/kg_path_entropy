""" A Python Class
A simple Python graph class to do essential operations into graph.
"""
from random import choice

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

        for possibility in self.__graph.nodes():
            if possibility != seed:
                if possibility not in self.__graph.successors(seed):
                    print(possibility, ' is not a sucessor')
                    prod = 1.0
                    print 'Degree', self.__graph.degree(possibility)
                    for i in range(self.__graph.degree(possibility)):
                        prod = prod * ((num_edges-self.__graph.degree(seed)+(-i+1)+1)/float(num_edges+(-i+1)+1))
                    print('Probability to have a connection', 1 - prod)

        # Print edges with relation
        # print DG.edges(data='relation')
