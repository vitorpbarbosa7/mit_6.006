from priorityqueueheap import PriorityQueue
from relaxation import try_to_relax

def dijkstra(Adj, s):
    '''
    Adj: Adjacency set with weights
    s: source vertex
    '''
    # initial shortest paths estimates
    d = {v: float('inf') for v in Adj}
    # parent pointers for each vertex
    parent = {v: None for v in Adj}
    # source distance and parent pointer
    d[s], parent[s] = 0, s
    # Initialize the Priority Queue
    Q = PriorityQueue()
    # Build the PriorityQueue with the vertex and the distance to the source
    for v in Adj:
        Q.insert(v, d[v])
    # Main loop to construct the d and parent objects
    for _ in range(len(Adj)):
        # Extract vertex with the minimun distance estimate to relax each edge adjacent to it
        u = Q.extract_min()
        # Iterate over each adjancent vertex to the minimun distance vertex
        for v in Adj[u]:
            # try to relax for each adjancet vertex
            try_to_relax(Adj, d, parent, u, v, s)
            # modify the adjancent vertex distance to the source, as the d object was updated in the relaxation process
            Q.decrease_key(v, d[v])
    return d, parent

if __name__ == '__main__':

    W = {
        's': {'a': 10, 'c': 3},
        'a': {'b': 2, 'c': 1},
        'b': {'d': 7},
        'c': {'a': 4, 'd': 2, 'b': 8},
        'd': {'b': 7}
    }
    s = 's'
    d, parent = dijkstra(W, s)
    print(d)
    print(parent)
