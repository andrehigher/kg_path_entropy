#!/usr/bin/env python
import sys
import networkx as nx
from util import Util
from graph import Graph

if __name__ == "__main__":
    # print sys.argv
    DG = nx.Graph()
    util = Util()
    graph = Graph(DG)
    util.read_file('dataset/fb15k/train.txt', graph)
    # util.read_file('dataset/nell/nell_cleaned.txt', graph)

    # graph.random_walk()
    # graph.predict_facts('tom_brady', 'new_england_patriots', 4)