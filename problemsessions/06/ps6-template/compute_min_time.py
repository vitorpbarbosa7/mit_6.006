
def dfs(Adj, s, parent = None, order = None):
    '''
    Adj: Adjacency list 
    s: start vertex
    '''

    # O(1) Initialize the parent list 
    if parent is None:
        # O(|V|) - use hash if unlabeled
        parent = {v: None for v in Adj}
        # O(1) - the root of the tree will be s, from which will follow to the other vertices, traversing them 
        parent[s] = s
        # O(1) - initialize empty array for the order of the vertices
        order = []

    for v in Adj[s]:
        # O(1) if no parent vertex exist for v yet in the parent list
        # if some adjacent node has already been visited, for example in previous stack call, it will backtrack, that is 
        # it will not enter into the another recursive call, it will not create a deeper level in the stack, but go back 
        # a level up in the stack 
        if parent[v] is None:
            # O(1) assign the s as parent vertex to v
            parent[v] = s
            # Recursive call, to, from the v which is in the Adjancy list of s
            # We go a deeper level to traverse the child nodes of v
            dfs(Adj, v, parent = parent, order=order)

   # in each stack append the source vertex 
    order.append(s)

    # It is returned the parent nodes from the tree which was constructed
    # from the depth first search algorithm starting from the first stack s vertex
    return parent, order

def full_dfs(Adj):
    # O(V) - use hash if unlabeled
    parent = {v: None for v in Adj}
    # O(1) - Initialize the order list
    order = []
    
    # O(V) Loop over every vertex in the graph
    for v in Adj:
        if parent[v] is None:
            # If it is the root, them assign as a parent (self root)
            # Will this make it possible to form a forest?
            parent[v] = v
            # So now we traverse in depth first search manner the graph with next depth vertex
            dfs(Adj, v, parent, order)

    return parent, order

def topological_order(dfs_return_order):
    return order[::-1]


if __name__ == '__main__':

    job_times = [('A', 1), ('B', 5), ('C', 5), ('D', 3), ('E', 4)],
    A2 = {
        7: [2, 6],
        2: [],
        6: [8],
        8: [5],
        5: [6],
    }
    
    parent, order = full_dfs(A2)
    print(parent)
    print(order)
    topo_order = topological_order(order)
    print(topo_order)

    hash_reference_index = {v: idx for idx, v in enumerate(topo_order)}
    print(hash_reference_index)
    # check the order of the u - v edges in the topological order
    for u in A2:
        for v in A2[u]:
            if hash_reference_index[u] < hash_reference_index[v]:
                print('Ok')
            else:
                raise Exception(f'Found a Cycle: {u}-{v}')

