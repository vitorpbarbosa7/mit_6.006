

class Graph:

    def __init__(self, Adj):
        self.Adj = Adj

    def __iter__(self):
        return iter(self.Adj)

    def itervertices(self):
        return iter(self.Adj)

    def inverse_neighbors(self, vertex):
        inv_neig = []
        # node will be the key
        # inside the edges we will have the nodes we will look for
        # and attribute as inv_neighbor of it the key node
        for node, edges in self.Adj.items():
            if node != vertex:
                for v, w in edges.items():
                    if v == vertex:
                        inv_neig.append(node)
        return inv_neig
    
    def weight(self, u, v):
        return self.Adj[u][v]
    
    def add_edge(self, u, v, weight):
        if u in self.Adj:
            # adding or overwriting it
            self.Adj[u][v] = weight
        else:
            self.Adj[u] = {}
            self.Adj[u][v] = weight


        

if __name__ == '__main__':
    Adj = {
        'A': {'C': 5, 'B': 5}, 
        'B': {}, 
        'C': {'B': 5, 'E': 4}, 
        'D': {'E': 4, 'B': 5}, 
        'E': {}
    }
    graph = Graph(Adj)
    graph.add_edge('F','G',4)
    breakpoint()
    print('iter vertices')
    [print(v) for v in graph.itervertices()]
    print('inverse neighbors')
    [print(v) for v in graph.inverse_neighbors('E')]

