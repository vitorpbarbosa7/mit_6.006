from dfs import dfs

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


if __name__ == '__main__':

    job_times = [('A', 2), ('B', 5), ('C', 5), ('D', 3), ('E', 4)]
    job_times = {job: time for job, time in job_times}
    edges = [('A', 'C'), ('C', 'B'), ('C', 'E'), ('D', 'E'), ('A', 'B'), ('D', 'B')]

    G = {v: {} for v, _ in job_times.items()}
    for s, t in edges:
        print(s, t)
        G[s][t] = job_times[t]
    
    # check vertex which have no parent pointers at all
    has_parent = set()
    for u in G:
        for v in G[v]:
            has_parent.add(v)
    
    not_parent = set()
    for vertex in G:
        if vertex not in has_parent:
            not_parent.add(vertex)

    print(s)
    breakpoint()
    distances, parent = dag_relaxation(G, s)
    print(distances)
    print(parent)

    # modify the weight for the source points and put them into a list for dag relaxation 
    for v in distances:
        if distances[v] == float('inf'):
            distances[v] = job_times[v]

    print(distances)


    