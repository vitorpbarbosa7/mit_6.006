from graph import Graph

class ShortestPathResult:
    def __init__(self):
        self.d = {}
        self.parent = {}

def shortest_path(graph:Graph, s):
    '''
    Single source shortest paths using DP on a DAG

    Args:
        graph: weighted DAG
        s: source
    '''

    result = ShortestPathResult()
    result.d[s] = 0
    result.parent[s] = None
    # lets get the distance from each vertex v to s
    # the s part is inside the result.d memo already 
    for v in graph.itervertices():
        sp_dp(graph, v, result)
    return result

def sp_dp(graph:Graph, v, result:ShortestPathResult):
    '''Recursion on finding the shortest path from v

    Args:
        graph: weighted DAG.
        v: a vertex in a graph
        result: for memoization and keeping track of the result
    '''

    print(f'\n--- Stack frame called for vertex: {v}')

    # check if the shortest path is already calculated for a certain vertex
    if v in result.d:
        print(f'Value of {result.d[v]} already calculated')
        return result.d[v]
    
    # if the result is not in the memo, let's recurse (top - bottom)
    result.d[v] = float('inf')
    result.parent[v] = None

    # u is a parent node 
    # v is the next node
    for u in graph.inverse_neighbors(v): 
        # this is a dag relaxation process using recursion and memoization
        # recursion: sp_dp -> traverse graph looking at adjacent nodes
        # memoization: keep track, in this case we are using even a class for that 
        # keep track of distance of each vertex from s to v and the parent node of v
        # coming from s 
        new_distance = sp_dp(graph, u, result) + graph.weight(u, v)
        if new_distance < result.d[v]:
            result.d[v] = new_distance
            result.parent[v] = u 
            print(f'new distance from {u}-{v} calculated of: {result.d[v]}')
    return result.d[v]
    
if __name__ == '__main__':
    Adj = {
        'A': {'C': 5, 'B': 5}, 
        'B': {}, 
        'C': {'B': 5, 'E': 4}, 
        'D': {'E': 4, 'B': 5}, 
        'E': {}
    }
    graph = Graph(Adj)

    result = shortest_path(graph, 'A')
    print(result.d)
    print(result.parent)


