
def dfs_topological_sort(Adj, s, visited, order):
    print('Stack frame created')
    print(f'Source vertex: {s}')
    breakpoint()
    visited[s] = True
    # if len(Adj[s]) > 0:
    #     print(Adj[s])
    #     breakpoint()
    for v in Adj[s]:
        if not visited[v]:
            dfs_topological_sort(Adj, v, visited, order)
    print(f'Vertex added to order: {s}')
    order.append(s)

def topological_sort(Adj):
    visited = [False] * len(Adj)
    order = []
    for v in range(len(Adj)):
        if not visited[v]:
            dfs_topological_sort(Adj, v, visited, order)
    return order[::-1]  # Reverse the order for topological sorting

# Example Adjacency List for the Company Hierarchy
Adj = [
    [3,5],
    [],
    [0,1],
    [],
    [1,2],
    []
]

# Run topological sort
top_order = topological_sort(Adj)

# Print the topological order
print("Topological Order (from lowest to highest):")
for i in top_order:
    print(f"Employee {i}")