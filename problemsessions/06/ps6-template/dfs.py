def dfs(Adj, s, parent=None, order=None):
    '''
    Adj: Adjacency list (with weights)
    s: start vertex
    '''

    if parent is None:
        parent = {v: None for v in Adj}
        parent[s] = s
        order = []

    # Iterate over each adjacent vertex and its weight
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent=parent, order=order)

    order.append(s)

    return parent, order