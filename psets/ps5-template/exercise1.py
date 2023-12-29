def dfs(Adj, s, visited, order):
    visited[s] = True
    for v in Adj[s]:
        if not visited[v]:
            dfs(Adj, v, visited, order)
    order.append(s)

def topological_sort(Adj):
    visited = {v: False for v in Adj}
    order = []
    for v in Adj:
        if not visited[v]:
            dfs(Adj, v, visited, order)
    return order[::-1]  # Reverse the order for topological sorting

# Example Adjacency List for the Company Hierarchy
AdjA = {
    'A': {'B'},
    'B': {'C', 'D'},
    'C': {'E', 'F'},
    'D': {'E','F'},
    'E': {},
    'F': {'F'}
}

AdjB = {
    'A': {'B'},
    'B': {'C', 'D'},
    'C': {'E', 'F'},
    'D': {'E'},
    'E': {},
    'F': {'D', 'F'}
}

# Run topological sort
top_order = topological_sort(AdjA)
print(top_order)

top_order = topological_sort(AdjB)
print(top_order)