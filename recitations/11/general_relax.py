
def general_relax(Adj, w, s):
    '''
    Adj:Adjacency list
    w: weights
    s: start
    '''

    # Shortest path initial estimates
    # This initial estimate will be relaxed
    d = [float('inf') for _ in Adj]

    # Initialize parent pointers 
    parent = [None for _ in Adj]

    # Initialize the source distance to itself
    d[s], parent[s] = 0, s
    
    # repeat forever
    while some_edge_relaxable(Adj, w, d):
        (u, v) = get_relaxable_edge(Adj, w, d)
        try_to_relax(Adj, w, d, parent, u, v)
    
    return d, parent
