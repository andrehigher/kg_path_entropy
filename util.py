""" A Python Class
A simple Python util class to do essential stuffs.
"""
import operator
import json
import networkx as nx
from collections import defaultdict

class Util():
    
    def read_file(self, file, graph, directed = True):
        """ A method to read the file and append to the
            graph the properly vertex and edges.
        """
        g = graph.get_graph()
        
        # EDGE TO BE PREDICTED 
        # V1 /m/01bpn - Bertrand Russell
        # V2 /m/02_xgp2 - Doctorate
        # L = 3
        v1 = '/m/01bpn'
        v2 = '/m/02_xgp2'
        L = 2

        with open(file, 'r') as f:
            for line in f:
                line2 = line.split('\t')
                line2[2] = line2[2][:-1]
                if directed == True:
                    g.add_edge(line2[0],line2[2],{'relation':line2[1]})
                else:
                    g.add_edge(line2[0],line2[2])
                
                if line2[0] == v1:
                    print(v1, line2[1], line2[2])

        edgesLen = float(len(g.edges()))
        nodesLen = float(len(g.nodes()))
        relations = nx.get_edge_attributes(g,'relation')
        print('Num of edges', edgesLen)
        print('Num of nodes', nodesLen)
        print('Degree of ', v1, g.degree(v1))
        print('Degree of ', v2, g.degree(v2))

        # print relations
        # print relations[('/m/01nczg', '/m/02lk60')]
        # /m/01bpn	/people/person/religion	/m/0kq2 
        # print relations[('/m/01bpn', '/m/0kq2')]
        # for key, value in relations.items():
        #     if key == ('/m/01nczg', '/m/02lk60'):
        #         print key, value

        print relations[('/m/01nczg', '/m/02lk60')]
        paths = nx.all_simple_paths(g, v1, v2, cutoff=L)
        paths = list(paths)
        print 'Number of paths from', v1, 'to', v2, ':', len(paths)
        # print '/m/01bpn', '/m/0kq2', relations[('/m/01bpn', '/m/0kq2')]

        for path in paths:
            # print(path)
            try:
                print 'paths', path[0], path[1]
                print 'relations hard', relations[('/m/01bpn', '/m/04g51')]
                print 'relations soft', relations[(str(path[0]), str(path[1]))]
                # if path[0] == '/m/01bpn' and path[1] == '/m/0kq2':
                #     print path[0], path[1]
                #     print relations[('/m/01nczg', '/m/02lk60')]
                #     print path[0], path[1], relations[(path[0], path[1])]
            except KeyError:
                pass

       

    def generate_edges_probabilities(self, store):
        """ A method to Generate dictionary for 
            edges distribution probability.
        """
        #store = {}
        # with open(file, 'r') as f:
        #     for line in f:
        #         line2 = line.split('\t')
        #         line2[2] = line2[2][:-1]
        #         ## Generate dictionary for edges distribution probability
        #         try:
        #             store[line2[1]]['count'] = store[line2[1]]['count'] + 1
        #             store[line2[1]]['probability'] = float(store[line2[1]]['count'])/(edgesLen)
        #         except KeyError as e:
        #             store[line2[1]] = { 'count': 1, 'probability': 1.0/(edgesLen), 'adjacent_edges': defaultdict(int) }
        #             store[line2[1]]
        # self.generate_edges_probabilities(store)
        # self.generate_edges_distribution(graph, store)
        sorted_store = sorted(store.items(), key=operator.itemgetter(1))
        with open('file.txt', 'w') as file:
            file.write(json.dumps(sorted_store))

    def generate_edges_distribution(self, graph, store):
        g = graph.get_graph()
        relations = nx.get_edge_attributes(g,'relation')

        for node in g.nodes():
            for neighbor in g.neighbors(node):
                try:
                    currentRelation = relations[(node, neighbor)]
                    for neighbor_neighbor in g.neighbors(neighbor):
                        store[currentRelation]['adjacent_edges'][relations[(neighbor, neighbor_neighbor)]] += 1
                except KeyError as e:
                    pass
        # print(store)
        for s in store:
            print(s, store[s]['count'])