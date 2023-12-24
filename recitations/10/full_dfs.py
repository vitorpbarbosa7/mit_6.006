
from dfs import dfs

def full_dfs(Adj):
    # O(V) - use hash if unlabeled
    parent = [None for v in Adj]
    # O(1) - Initialize the order list
    order = []
    
    # O(V) Loop over every vertex in the graph
    for v in range(len(Adj)):
        if parent[v] is None:
            # If it is the root, them assign as a parent (self root)
            # Will this make it possible to form a forest?
            parent[v] = v
            # So now we traverse in depth first search manner the graph with next depth vertex
            dfs(Adj, v, parent, order)

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

    parent, order = full_dfs(A2)
    print(parent)
    print(order)

    Adj = [
    [],         # CEO has no one above them (index 0)
    [0],        # VP 1 reports to CEO (index 1)
    [0],        # VP 2 reports to CEO (index 2)
    [0],        # VP 3 reports to CEO (index 3)
    [1],        # Manager 1 reports to VP 1 (index 4)
    [1],        # Manager 2 reports to VP 1 (index 5)
    [2],        # Manager 3 reports to VP 2 (index 6)
    [3],        # Manager 4 reports to VP 3 (index 7)
    [4],        # Employee 1 reports to Manager 1 (index 8)
    [5],        # Employee 2 reports to Manager 2 (index 9)
    [6],        # Employee 3 reports to Manager 3 (index 10)
    [7],        # Employee 4 reports to Manager 4 (index 11)
]
    
    _, order = full_dfs(Adj)

    print(order[::-1])

