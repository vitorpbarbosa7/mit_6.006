from dfs import dfs

def full_dfs(Adj):
    num_vertices = len(Adj)
    parent = [None for _ in range(num_vertices)]
    order = []
    components = []  # List to store connected components

    # for each vertex in the graph (because this is full dfs)
    for v in range(num_vertices):
        # if not visited yet
        if parent[v] is None:
            parent[v] = v
            dfs_start = len(order)  # Record the start position of this component in 'order'

            # A full stack call to Depth First Search will mean we will have those connected components
            # For a new call of the first level of the function, then it will be a new connected component in the graph 
            # that happens because from a start vertex v will will be able to reach all the others if in a connected component?
            dfs(Adj, v, parent, order)

            # that is it, when exit a stack call of dfs, it means visited all nodes reachable from a v node from which started, that means, this is a connected component

            # this order keeps the order in which they are being visited 
            # it will be collection of clumps at the end
            # but as exploring, a single clump will correspond to the start of this exploration (dfs_start) till what have explored so far in this dfs stack call 
            component = order[dfs_start:]  # Extract the component based on 'order'
            components.append(component)

    return parent, order, components


if __name__ == '__main__':
    A2 = [
        [],
        [2,4],
        [5],
        [5,6],
        [2],
        [4],
        []
    ]

    parent, order, components = full_dfs(A2)
    print("Parent:", parent)
    print("Order:", order)
    print("Connected Components:", components)