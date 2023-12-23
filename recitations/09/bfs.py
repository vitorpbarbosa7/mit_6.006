
def bfs(Adj, s):
    '''
    Adj: Adjancency list
    s: starting vertex

    Returns:
    The parent nodes of s
    '''

    # O(V) (use hash if unlabeled vertices)
    # Initially all nodes have no parents, by the bfs algorithm 
    # Them, by finding the parents, we will find the paths
    parent = [None for v in Adj]
    # O(1) root node s
    parent[s] = s
    # O(1) Initialize levels 
    level = [[s]]
    # 
    while 0 < len(level[-1]):
        # O(1) make new level, as has already explored all previous adjancy nodes in previous level
        # Runs in ammortized with the python list dynamic array implementation
        level.append([])
        # Loop over the level, through every vertex u (to find the adjancency nodes)
        for u in level[-2]:
            # vs are the adjancy nodes of u
            for v in Adj[u]:
                # Do not allow duplicates of parent node (more than one path from a node to another)
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)

    return parent, level

def unweighted_shortest_path(Adj, s, t):

    # O(V + E) BFS tree from s ( s as root)
    parent, _ = bfs(Adj, s)
    # O(1) t reachable from s?
    # we can not reach s from t if t has no parent node
    if parent[t] is None:
        return None
    # Label of current vertex
    i = t
    # Start at t
    path = [t]
    # go back for each parent, untill reach s
    while i != s:
        print(parent[i])
        breakpoint() 
        i = parent[i]
        path.append(i)
    
    # O(|V|) return reversed path (we went from t to s?)
    return path[::-1]



if __name__ == '__main__':

    A2 = [
        [1,4,3],
        [0],
        [3],
        [0,2],
        [0]
    ]
    s = 0

    paths, levels = bfs(A2, s)

    # shortest path
    t = 2
    path = unweighted_shortest_path(A2, s, t)
    print(path)

