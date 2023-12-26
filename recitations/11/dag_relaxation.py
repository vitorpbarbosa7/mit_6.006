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

    # The topological sort order, got from Depth First Search, guarantees that
    # the relaxation, that is, trying to find the new best shortest path
    # will occur in the order they appear in the graph, in a possible right path 
    for u in topological_order:
        for v in Adj[u]:

            print(f'{u} : {Adj[u]}')
            try_to_relax(Adj, w, d, parent, u, v, s)
    
    return d, parent

def try_to_relax(Adj, w, d, parent, u, v, s):

    old_d = d[v]
    if d[v] > d[u] + w(Adj, u, v):
        print(f'\nNew path found, because')
        print(f'{d[v]} > {d[u]} + {w(Adj, u, v)}')
        d[v] = d[u] + w(Adj, u, v)
        print(f'distance from {s} to {v} updated from {old_d} to {d[v]}')

        # update new parent pointer for v, which will come from u
        # since we found a new path 
        parent[v] = u

def w(Adj, u, v):

    return Adj[u][v]




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
    
    d, parent = dag_relaxation(W, s)
    
    print(f'\nDistances from s to connected vertices:\n {d}')
    print(f'\n Parent pointers:\n {parent}')