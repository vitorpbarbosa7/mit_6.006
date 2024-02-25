def bfs(Adj, s, parent):
    '''
    Adj: Adjacency list
    s: starting vertex
    parent: list to store parent nodes
    '''
    # Initialize levels 
    level = [[s]]
    parent[s] = s
    
    while 0 < len(level[-1]):
        level.append([])
        # for each node in the current level 
        for u in level[-2]:
            # for each adjancent node in of that single vertex in the current level
            for v in Adj[u]:
                if parent[v] is None:
                    # the parent of the v is u
                    parent[v] = u
                    # and v will be added to the last level 
                    level[-1].append(v)

def full_bfs(Adj):
    num_vertices = len(Adj)
    parent = [None for _ in range(num_vertices)]
    order = []

    bfs_calls = 0
    for v in range(num_vertices):
        if parent[v] is None:
            bfs_calls += 1
            print(bfs_calls)

            # breadth first search, runs from a single vertex to all vertex from which it can reach
            # keeping parent pointers from each node
            # running full breatdh first search accounts for all nodes
            # but if already visited, will not be computed again
            # the line of 'if parent[v] is None' accounts for that   
            bfs(Adj, v, parent)
            order.append(v)  # Optional: Record the order of BFS calls

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

    parent, order = full_bfs(A2)
    print("Parent:", parent)
    # does this corresponds to topological order ?
    print("Order of BFS calls:", order)
