def w(Adj, u, v):
    '''
    Get the weight between to adjacent vertices
    '''
    return Adj[u][v]

def try_to_relax(Adj, d, parent, u, v, s):

    # trying to find new paths with less weight

    # print(f'Try to find relax {u}-{v}')
    # breakpoint()
    old_d = d[v]
    if d[v] > d[u] + w(Adj, u, v):
        # print(f'\nNew path found, because')
        # print(f'{d[v]} > {d[u]} + {w(Adj, u, v)}')
        d[v] = d[u] + w(Adj, u, v)
        # print(f'distance from {s} to {v} updated from {old_d} to {d[v]}')

        # update new parent pointer for v, which will come from u
        # since we found a new path 
        parent[v] = u

def bellman_ford(Adj, s):
    '''
    Adj: adjacency set
    w: weights
    s: start vertex
    '''

    # a number greater than the sum of all weights
    infinity = float('inf')
    # initial shortest path estimates
    d = {v: infinity for v in Adj}
    # Initialization for parent points of each vertex
    parent = {v: None for v  in Adj}
    # Initialize the parent and distance of the source vertex
    d[s], parent[s] = 0, s

    # construct shortest path in rounds
    # Number of vertices
    V = len(Adj)
    # Process to relax all edges in |V| - 1 steps
    # So it passes through every edge |V| times
    for k in range(V - 1):
        # print(f'k {k} iteration to relax the edges')
        # breakpoint()
        for u in Adj:
            for v in Adj[u]:
                try_to_relax(Adj, d, parent, u, v, s)

    # check for negative weight cycles accessible from s
    for u in Adj:
        # breakpoint()
        for v in Adj[u]:
            if d[v] > d[u] + w(Adj, u,v):
                # raise Exception('Ack ! There is a negative weight cycle')
                print('Ack ! There is a negative weight cycle')
                return None
    
    # return d, parent
    return d

if __name__ == '__main__':

    # this one contains negative cycle
    W = {
        'a': {'b': -5, 'c': 6},
        'b': {'c': -4},
        'c': {'d': 3},
        'd': {'b': -1},
    }

    s = 'a'
    # bellman_ford(W, s)

    # this one does not contain negative cycle
    W2 = {
        'a': {'b': -5, 'e': 7},
        'b': {'e': 6, 'f': -4},
        'c': {},
        'd': {'c': 5},
        'e': {'f': 3},
        'f': {'g': 2, 'c': 8},
        'g': {'c': 1, 'h': -2},
        'h': {'c': 9, 'd': 4}
        }
    
    d, parent = bellman_ford(W2, s)
    # print(d)
    # print(parent)

# intuitions about why need the |V| rounds
# The Bellman-Ford algorithm is designed to handle graphs with negative weight edges and can also detect negative weight cycles. The key part of the algorithm is the relaxation process, where it iteratively relaxes the edges to find the shortest paths from a starting vertex to all other vertices in the graph. Here's some intuition behind why the algorithm needs |V| - 1 rounds (where |V| is the number of vertices in the graph) to relax all edges:

# Propagation of Shortest Paths: In the worst case, the shortest path from the starting vertex to some other vertex in the graph might pass through every other vertex. This means it could take |V| - 1 edges (since the shortest path in a graph with |V| vertices can have at most |V| - 1 edges, due to the definition of a path in a graph). The algorithm needs enough iterations to allow a shortest path that goes through all these vertices to propagate through the network.

# Gradual Update of Distance Estimates: Bellman-Ford works by gradually improving the estimate of the shortest distance to each vertex. In each iteration, it relaxes all edges, potentially updating the shortest path estimate for some vertices. However, a single iteration might not be enough for the shortest path information to propagate from the source to all vertices, especially if the shortest path involves multiple edges.

# Ensuring Convergence: After |V| - 1 iterations, the algorithm has effectively considered all possible paths between the source and every other vertex (since a path longer than |V| - 1 edges would imply a cycle). Therefore, if the graph doesn't contain a negative weight cycle that is reachable from the source, the shortest paths will have stabilized by this point.

# Detecting Negative Weight Cycles: If, after |V| - 1 iterations, the algorithm finds that it can still relax an edge, it means there is a negative weight cycle in the graph. This is because the only way to further reduce the distance estimate is if there's a cycle that cumulatively reduces the path length.

# In summary, the |V| - 1 iterations ensure that the Bellman-Ford algorithm has had enough time to propagate the shortest path information through all possible paths in the graph (considering the longest possible path without cycles in a graph is |V| - 1 edges long). This is why it's sufficient and necessary for finding the shortest paths in a graph, even in the presence of negative weight edges.
    


# DAGS
    
# if it was a dag, would it be easier, and use topological sort and only one round would solve it already ? 

# Yes, if the graph is a Directed Acyclic Graph (DAG), finding the shortest paths from a single source becomes significantly simpler and more efficient. In a DAG, you can use a topological sort to order the vertices in a linear order such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

# Here's why a single pass is enough in a DAG after a topological sort:

# No Cycles: Since the graph is acyclic, there are no cycles. This property means that once you have computed the shortest path to a vertex, it does not need to be updated again because there's no way to get back to that vertex via another path and find a shorter route.

# Topological Order: When the vertices are sorted in topological order, each edge is considered only after computing the shortest paths to its source vertex. This ensures that when an edge is relaxed, the shortest path to its source has already been found.

# Efficient Path Propagation: In topological order, you're effectively propagating the shortest path information in the most efficient way possible. As you iterate through the vertices, you're relaxing the edges leading out of each vertex. Since there are no cycles and each vertex is considered after all vertices leading into it, this guarantees that all shortest paths from the source to each vertex are correctly computed in this single pass.

# The algorithm for finding the shortest paths in a DAG is thus:

# Perform a topological sort of the graph.
# Initialize distances to all vertices as infinite and distance to the source as 0.
# Traverse the vertices in topological order. For every vertex, relax all edges going out from it.
# This method is much more efficient compared to the Bellman-Ford algorithm for a DAG, as it only requires a single pass through the vertices following the topological sort, rather than |V| - 1 passes through all the edges.    

