def dfs_topological_sort(Adj, s, visited, order):
    visited[s] = True
    for v in Adj[s]:
        if not visited[v]:
            dfs_topological_sort(Adj, v, visited, order)
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

# Run topological sort
top_order = topological_sort(Adj)

# Print the topological order
print("Topological Order (from lowest to highest):")
for i in top_order:
    print(f"Employee {i}")