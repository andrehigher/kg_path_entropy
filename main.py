#!/usr/bin/env python
import sys
import networkx as nx
from util import Util
from graph import Graph

if __name__ == "__main__":
    # print sys.argv
    DG=nx.DiGraph()
    util = Util()
    graph = Graph(DG)
    util.read_file('dataset/fb15k/train.txt', graph)
    graph.random_walk()