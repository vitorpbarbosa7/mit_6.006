from collections import defaultdict, deque

def topological_sort(Adj):
    in_degree = {u: 0 for u in Adj}
    for u in Adj:
        for v in Adj[u]:
            in_degree[v] += 1

    queue = deque([u for u in Adj if in_degree[u] == 0])
    top_order = []

    while queue:
        u = queue.popleft()
        top_order.append(u)

        for v in Adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return top_order

def shortest_path(Adj, start):
    top_order = topological_sort(Adj)
    distance = {v: float('inf') for v in Adj}
    distance[start] = 0

    for u in top_order:
        for v, weight in Adj[u].items():
            if distance[v] > distance[u] + weight:
                distance[v] = distance[u] + weight

    return distance

def find_min_stress_path(Adj, target):
    distance = shortest_path(Adj, target)
    min_stress = float('inf')
    min_stress_class = None

    for u in Adj:
        if not Adj[u] and distance[u] < min_stress:
            min_stress = distance[u]
            min_stress_class = u

    return min_stress_class, min_stress

# Test Example (A simplified version with a smaller set of classes for demonstration)
Adj = {
    '19.854': {},  # Target course with prerequisites from level 4
    # Level 1: Foundational Courses
    '101': {}, '102': {}, '103': {}, '104': {}, '105': {},
    # Level 2: Intermediate Courses
    '201': {'101': 2}, '202': {'102': 2}, '203': {'103': 3}, '204': {'104': 1}, '205': {'105': 4},
    # Level 3: Advanced Courses
    '301': {'201': 2, '202': 1}, '302': {'202': 3}, '303': {'203': 2}, '304': {'204': 4}, '305': {'205': 3},
    # Level 4: Specialized Courses
    '401': {'301': 5, '302': 2}, '402': {'302': 3, '303': 2}, '403': {'303': 4, '304': 1},
    '404': {'304': 3}, '405': {'305': 2},
    # Level 5: Expert Courses (leading to '19.854')
    '501': {'401': 2, '402': 1}, '502': {'402': 3, '403': 2}, '503': {'403': 3}, '504': {'404': 4},
    '505': {'405': 1}, '19.854': {'501': 3, '502': 4, '503': 2, '504': 5, '505': 1}
}


target_class = '19.854'
min_stress_class, min_stress = find_min_stress_path(Adj, target_class)

print(f"Minimum Stress Class: {min_stress_class} with stress: {min_stress}")