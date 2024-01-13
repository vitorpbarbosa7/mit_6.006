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
    # D = [[INF for _ in range(n)] for _ in range(n)]
    edges = S
    # print(edges)
    # breakpoint()

    source_cities = [v[0] for v in edges]
    target_cities = [v[1] for v in edges]
    all_cities = set(source_cities + target_cities)
    # print(all_cities)
    # breakpoint()
    Gw = {v: {} for v in all_cities}
    for ss, tt, weight in edges:
        Gw[ss][tt] = weight
    # printG(Gw)
    # breakpoint()

    # construct Gs by adding the super node s connected to each v of V with 0 weight edge
    sn = 's'
    Gs = dict(Gw)
    Gs[sn] = {}
    for v in Gw:
        Gs[sn][v] = 0
    # printG(Gs)

    # Compute Shortest Path from Super Node S for every v of V using BellmanFord
    dbf = bellman_ford(Gs, sn)
    if dbf is None:
        return
    # print('\n dbf')
    # print(dbf, '\n')

    # Reweight each edge w'(u,v) = w(u,v) + ∂s(s,u) - ∂s(s,v)
    Gp = dict(Gw)
    for u in Gp:
        for v in Gp[u]:
            # print(Gw[u][v])
            # print(dbf[u])
            # print(dbf[v])
            # breakpoint()
            Gp[u][v] = Gw[u][v] + dbf[u] - dbf[v]
    # printG(Gp)

    # for each u 𝜀 V compute Shortest Path Distances in Gp using Dijkstra
    dd = {v: INF for v in Gp}
    for v in Gp:
        dd[v], _ = dijkstra(Gp, v)
    # print('\n shortest paths after Dijkstra in positive weights graph:')
    # print('dd')
    # print(dd, '\n')

    # make the correction on the positive weight graph to correspond to distances in original graph 
    dw = {v: {v: INF for v in Gw} for v in Gw}
    for v in Gw:
        dw[v][v] = 0
    # print('\n initialized distances for final calculation')
    # print(dw, '\n')

    for u in Gw:
        for v in Gw:
            # print(f' {u}-{v}')
            # print(f'dbf[u]: {dbf[u]}')
            # print(f'dbf[v]: {dbf[v]}')
            # breakpoint()
            new_distance = dd[u][v] - dbf[u] + dbf[v]
            dw[u][v] = min(dw[u][v], new_distance)
    # print(dw)

    rows = [list(d.values()) for _, d in dw.items()]
    # print(rows)
    D = tuple(tuple(row) for row in rows)
    # print(D)

    return D


if __name__ == '__main__':
    inputs = [
        ((0, 1, -1), (0, 2, -2), (1, 3, -5), (2, 1, -3), (2, 3, -4)),
        ((0, 1, -6), (0, 2, 3), (1, 3, 1), (2, 1, -5), (3, 2, 2))
    ]

    res = []
    for input in inputs:
        res.append(johnson(0, input))

    