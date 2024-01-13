from bellman_ford import bellman_ford 
from dijkstra import dijkstra

def printG(G):
    print('\n\nGraph:')
    for k, v in G.items():
        print(k, v)
    print('\n\n')

INF = 99999     # distance magnitudes will not be larger than this number
def johnson(n, S):
    '''
    Input:  n | Number of vertices in the graph
            S | Tuple of triples (u, v, w) representing edge (u, v) of weight w
    Output: D | Tuple of tuples where D[u][v] is the distance from u to v
              |   or INF if v is not reachable from u
              |   or None if the input graph contains a negative-weight cycle
    '''
    D = [[INF for _ in range(n)] for _ in range(n)]

    
    D = tuple(tuple(row) for row in D)
    return D

# construct the graph adjacency structure
edges = ((0, 1, -1), (0, 2, -2), (1, 3, -5), (2, 1, -3), (2, 3, -4)),
source_cities = [v[0] for v in edges[0]]
target_cities = [v[1] for v in edges[0]]
all_cities = set(source_cities + target_cities)
print(all_cities)
Gw = {v: {} for v in all_cities}
for ss, tt, weight in edges[0]:
    Gw[ss][tt] = weight
printG(Gw)

# construct Gs by adding the super node s connected to each v of V with 0 weight edge
sn = 's'
Gs = dict(Gw)
Gs[sn] = {}
for v in Gw:
    Gs[sn][v] = 0
printG(Gw)

# Compute Shortest Path from Super Node S for every v of V using BellmanFord
dbf, pbf = bellman_ford(Gs, sn)
print(dbf)
# print(pbf)

#TODO check for negative weight cycle and return None if it happens 

# Reweight each edge w'(u,v) = w(u,v) + ∂s(s,u) - ∂s(s,v)
Gp = dict(Gw)
for u in Gp:
    for v in Gp[u]:
        Gp[u][v] = Gw[u][v] + dbf[u] - dbf[v]
printG(Gp)

# for each u 𝜀 V compute Shortest Path Distances in Gp using Dijkstra
dd = {v: float('inf') for v in Gp}
for v in Gp:
    dd[v], _ = dijkstra(Gp, v)
print(dd)

# compute ∂(u,v) = ∂'(u,v) - ∂s(s,u) + ∂s(s,v)
dw = {v: {} for v in Gp}
for u in Gw:
    for v in Gw[u]:
        dw[u][v] = dd[u][v] - dbf[u] + dbf[v]
print(dw)






























