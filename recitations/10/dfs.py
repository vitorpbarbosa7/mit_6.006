def dfs(Adj, s, parent = None, order = None):
    '''
    Adj: Adjacency list 
    s: start vertex
    '''

    # O(1) Initialize the parent list 
    if parent is None:
        # O(|V|) - use hash if unlabeled
        parent = [None for v in Adj] 
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

if __name__ == '__main__':

    A2 = [
        [],
        [2,4],
        [5],
        [5,6],
        [2],
        [4],
        []
    ]
    s = 1

    parent, order = dfs(A2, s)
    print(parent)
    print(order)
