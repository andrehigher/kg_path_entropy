#!/usr/bin/env python
import sys
import networkx as nx
from util import Util
from graph import Graph

if __name__ == "__main__":
    # print sys.argv
    DG=nx.DiGraph()
    # DG=nx.Graph()
    util = Util()
    graph = Graph(DG)
    util.read_file('dataset/NELL.08m.130.SSFeedback.csv', graph)
    # graph.random_walk()
    graph.entropy('tom_brady', 'football')
    