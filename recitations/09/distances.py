
from bfs import unweighted_shortest_path

def all_distances(Adj):
    num_vertices = len(Adj)
    d = {v: 0 for v in range(num_vertices)}
    R = float('inf')
    for s in range(num_vertices):
        for t in range(num_vertices):
            path = unweighted_shortest_path(Adj, s, t)
            if path is not None:
                r_path = len(path)
            else:
                0
            d[s] = max(d[s], r_path)
    return d

if __name__ == '__main__':
    
    W = [
        [1,4],
         [4, 5],
         [],
         [2],
         [5],
         [6, 2],
         [2, 7],
         [2, 3]
    ]

    d = all_distances(W)
    print(d)

    radius = min(d.values())
    print(radius)