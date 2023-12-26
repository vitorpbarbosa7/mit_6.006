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
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    parent[v] = u
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
    print("Order of BFS calls:", order)
