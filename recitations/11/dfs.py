def dfs(Adj, s, parent=None, order=None):
    '''
    Adj: Adjacency list (with weights)
    s: start vertex
    '''
    # print(f'Stack frame created')

    # Base case for root 
    if parent is None:
        parent = {vv: None for vv in Adj}
        parent[s] = s
        order = []

    # Iterate over each adjacent vertex and its weight
    for v in Adj[s]:
        # print(f'Vertex: {v}')
        # print(f'Parent: {s}')
        # print(f'Parent dict: {parent}')


        # c is the first one added, so c already has a parent and it was visited
        # therefore it will not be visited again
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent=parent, order=order)

    # print('Will add now')
    # print('Will add the last first, and so on')
    order.append(s)
    # print(order)

    return parent, order


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

    parent, order = dfs(W, s)

    topological_order = order.reverse()
    # print(topological_order)
    print(parent)
    print(order)
