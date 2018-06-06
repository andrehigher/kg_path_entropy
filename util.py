""" A Python Class
A simple Python util class to do essential stuffs.
"""
import operator
import json

class Util():
    
    def read_file(self, file, graph, directed = True):
        """ A method to read the file and append to the
            graph the properly vertex and edges.
        """
        g = graph.get_graph()
        store = {}
        with open(file, 'r') as f:
            for line in f:
                line2 = line.split('\t')
                line2[2] = line2[2][:-1]
                if directed == True:
                    g.add_edges_from([(line2[0],line2[2],{'relation':line2[1]})])
                else:
                    g.add_edge(line2[0],line2[2])

                ## Generate dictionary for edges distribution probability
                try:
                    store[line2[1]] = store[line2[1]] + 1
                except KeyError as e:
                    store[line2[1]] = 1

        self.generate_edges_probabilities(store)

    def generate_edges_probabilities(self, store):
        """ A method to Generate dictionary for 
            edges distribution probability.
        """
        sorted_store = sorted(store.items(), key=operator.itemgetter(1))
        with open('file.txt', 'w') as file:
            file.write(json.dumps(sorted_store))
