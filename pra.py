#!/usr/bin/env python
import sys
import networkx as nx
from util import Util
from graph import Graph

if __name__ == "__main__":
    DG=nx.DiGraph()
    util = Util()
    graph = Graph(DG)
    util.read_file('dataset/nell/NELL.08m.130.SSFeedback.csv', graph)
    graph.entropy('tom_brady', 'football')
    