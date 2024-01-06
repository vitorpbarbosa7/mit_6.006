def dfs(Adj, s, parent=None, order=None):
    if parent is None:
        parent = [None for v in Adj]
        parent[s] = s
    if order is None:
        order = []
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order

def topo_shortest_paths(Adj, w, s):
    _, order = dfs(Adj, s)
    order.reverse()
    d = [float('inf') for _ in Adj]
    parent = [None for _ in Adj]
    d[s], parent[s] = 0, s
    for u in order:
        for v in Adj[u]:
            if d[v] > d[u] + w(u, v):
                d[v] = d[u] + w(u, v)
                parent[v] = u
    return d, parent

def min_time(C, D):
    n = len(C)
    file_idx, file_time = {}, {}
    for i in range(n):  # label files from 1 to n
        f, t = C[i]
        file_idx[f], file_time[i + 1] = i + 1, t
    Adj, w = [[] for _ in range(n + 1)], {}  # construct dependency graph
    for f1, f2 in D:
        i1, i2 = file_idx[f1], file_idx[f2]
        Adj[i1].append(i2)
        w[(i1, i2)] = -file_time[i2]
    Adj[0] = list(range(1, n + 1))  # add supernode
    for i in range(1, n + 1):
        w[(0, i)] = -file_time[i]
    _, order = dfs(Adj, 0)  # check for cycles
    order.reverse()
    rank = [None] * (n + 1)
    for i in range(n + 1):
        rank[order[i]] = i
    for v1 in range(n + 1):
        for v2 in Adj[v1]:
            if rank[v1] > rank[v2]:
                return None
    dist, _ = topo_shortest_paths(Adj, lambda u, v: w[(u, v)], 0)

    #debug
    print('\n')
    print(dist)
    return -min(dist)  # compute min time
