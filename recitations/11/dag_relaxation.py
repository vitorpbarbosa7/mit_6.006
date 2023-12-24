from dfs import dfs

def dag_relaxation(Adj, s):
    # Depth First Search returns an order of the graph
    _, order = dfs(Adj, s)
    # order reverse to have the topological sort order form the source s 
    order.reverse()
    topological_order = order
    # initialize all initial estimates of distance as infinity 
    d = {v: float('inf') for v in Adj}
    # Initialize parent pointer for every vertex
    parent = {v: None for v in Adj}
    # Source vertex parent pointer is each self, s, and distance to itself is 0
    d[s], parent[s] = 0, s

    for u in topological_order:
        for v in Adj[u]:

            print(f'{u} : {Adj[u]}')
            # try_to_relax(Adj, w, d, parent, u, v)
    
    return d, parent


if __name__ == '__main__':

    W = {
        'a': {'b': -5, 'e': 7},
        'b': {'e': 6, 'f': -4},
        'c': {},
        'd': {'c': 5},
        'e': {'f': 3},
        'f': {'g': 2, 'c': 8},
        'g': {'c': 1, 'h': -2},
        'h': {'c': 9, 'd': 4}
        }
    
    s = 'e'
    
    dag_relaxation(W, s)