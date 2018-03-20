import sys
from graph import Graph

if __name__ == "__main__":
    # print sys.argv
    
    graph = Graph()
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())