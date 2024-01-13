def try_to_relax(Adj, d, parent, u, v, s):

    # trying to find new paths with less weight

    old_d = d[v]
    if d[v] > d[u] + w(Adj, u, v):
        # print(f'\nNew path found, because')
        # print(f'{d[v]} > {d[u]} + {w(Adj, u, v)}')
        d[v] = d[u] + w(Adj, u, v)
        # print(f'distance from {s} to {v} updated from {old_d} to {d[v]}')

        # update new parent pointer for v, which will come from u
        # since we found a new path 
        parent[v] = u

def w(Adj, u, v):
    return Adj[u][v]