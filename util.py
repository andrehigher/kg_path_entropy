""" A Python Class
A simple Python util class to do essential stuffs.
"""

class Util():
    
    def read_file(self, file, graph):
        """ A method to read the file and append to the
            graph the properly vertex and edges.
        """
        g = graph.get_graph()
        with open(file, 'r') as f:
            for line in f:
                line2 = line.split('\t')
                line2[2] = line2[2][:-1]
                g.add_edges_from([(line2[0],line2[2],{'relation':line2[1]})])
