from dfs import dfs
from set_dfs_topological_order_detect_cycle import topological_order 

def dag_relaxation(Adj, s):
    # Depth First Search returns an order of the graph
    _, order = dfs(Adj, s)
    # order reverse to have the topological sort order form the source s 
    order.reverse()
    topological_order = order
    # initialize all initial estimates of distance as infinity 
    d = {v: float('inf') for v in Adj}
    # Initialize parent pointer for every vertex
    parent = {v: None for v in Adj}
    # Source vertex parent pointer is each self, s, and distance to itself is 0
    d[s], parent[s] = 0, s

    # The topological sort order, got from Depth First Search, guarantees that
    # the relaxation, that is, trying to find the new best shortest path
    # will occur in the order they appear in the graph, in a possible right path 
    for u in topological_order:
        for v in Adj[u]:

            print(f'{u} : {Adj[u]}')
            try_to_relax(Adj, d, parent, u, v, s)
    
    return d, parent

def try_to_relax(Adj, d, parent, u, v, s):

    # trying to find new paths with less weight

    old_d = d[v]
    if d[v] > d[u] + w(Adj, u, v):
        print(f'\nNew path found, because')
        print(f'{d[v]} > {d[u]} + {w(Adj, u, v)}')
        d[v] = d[u] + w(Adj, u, v)
        print(f'distance from {s} to {v} updated from {old_d} to {d[v]}')

        # update new parent pointer for v, which will come from u
        # since we found a new path 
        parent[v] = u

def w(Adj, u, v):
    return Adj[u][v]

def printG(G):
    print('\n\nG')
    for k, v in G.items():
        print(k, v)
    print('\n\n')


if __name__ == '__main__':

    # Construct Graph
    job_times = [('A', 1), ('B', 5), ('C', 5), ('D', 3), ('E', 4)]
    job_times = {job: time for job, time in job_times}

    # --> make all times negative:
    job_times = {job: -time for job, time in job_times.items()}
    edges = [('A', 'C'), ('C', 'B'), ('C', 'E'), ('D', 'E'), ('A', 'B'), ('D', 'B')]
    G = {v: {} for v, _ in job_times.items()}
    for s, t in edges:
        print(s, t)
        G[s][t] = job_times[t]    
    printG(G)
    G['S'] = {}
    for v, t in job_times.items():
        G['S'][v] = t
    printG(G)

    # Detect cycle
    _, order = dfs(G, 'S')
    topo_order = topological_order(order)
    print(topo_order)
    topo_order = {v: idx for idx, v in enumerate(topo_order)}
    rank = {v: None for v in G} 
    for v in G:
        position = topo_order[v]
        rank[v] = position
    # print(f'\n\nPosition of each vertex in the topological order: \n {rank}\n\n')
    for u in G:
        for v in G[u]:
            if rank[u] > rank[v]:
                # return None
                raise Exception("Found don't know what")

    # The min distance comes from here
    dist, _ = dag_relaxation(G, 'S')
    print(dist)
    dist_array = [d for _, d in dist.items()]
    print(dist_array)
    print(min(dist_array))

