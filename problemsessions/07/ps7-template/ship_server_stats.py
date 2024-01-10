from dfs import dfs
from maxpriorityqueueheap import PriorityQueueMaxHeap
from dijkstra import dijkstra

def try_to_relax_bottleneck(Adj, d, u, v, s):
    # initially all possible capacities are understimates to be 0
    # similar to in a path, in which we are initially pessimit about not being able to reach t from s, that is, set them to +inf distance

    # the relaxation process will check what is the maximum 
    # maximum bottleneck to node v was this d[v]
    # now let's check if reaching v from u we get a larger value

    minimum_capacity_from_u_to_v = min(d[u], w(Adj, u, v))
    # if reaching v from u is less than the value before, we keep the old one
    # if reaching v from u is more than the value before, we update
    old_d = d[v]
    if d[v] < minimum_capacity_from_u_to_v:
        print(f'\nFrom {u} to {v}')
        print(f'New max bottleneck found, because ')
        print(f'{minimum_capacity_from_u_to_v} > {d[v]}')
        print(f'Better to come to {v} from the {u} vertex, since the bottleneck of this new path is larger than the bottleneck of the old path to reach v')
        d[v] = max(d[v], minimum_capacity_from_u_to_v)
        print(f'capacity from {s} to {v} updated from {old_d} to {d[v]}')
    else:
        print('ELSE CLAUSE')
        print(f'New bottleneck is less than the old bottleneck: {minimum_capacity_from_u_to_v} < {d[v]}')

def w(Adj, u, v):
    return Adj[u][v]

def dijkstra_bottleneck(Adj, s):
    '''
    Adj: Adjacency set with weights
    s: source vertex
    '''
    # initial possible weights to be carried from d to other vertices
    d = {v: 0 for v in Adj}
    # full capacity, perfectly possible to carry the object to the same location
    d[s] = float('inf')
    # Initialize the Priority Queue 
    # If in the distance problem the priority is given to the shortest distance vertex coming from s 
    # now the priority is about the maximum bottleneck considering all possible weight of trucks to be carried? - let's call it capacity
    Q = PriorityQueueMaxHeap()
    # Build the PriorityQueue with the vertex and the distance to the source
    for v in Adj:
        Q.insert(v, d[v])
    # Main loop to construct the capacities, that is, the maximum bottlenecks to reach of the vertices from s
    for _ in range(len(Adj)):
        # Extract vertex with maximum capacity to continue the relaxation process to find the maximum bottleneck
        print(f'\n Current Priority Queue')
        print(Q)
        u = Q.extract_max()
        print(f'Extracted vertex to explore frontier {u}')
        # Iterate over each adjancent vertex to the minimun distance vertex
        for v in Adj[u]:
            # try to relax for each adjancet vertex
            try_to_relax_bottleneck(Adj, d, u, v, s)
            # modify the adjancent vertex distance to the source, as the d object was updated in the relaxation process
            Q.decrease_key(v, d[v])
    return d

def ship_server_stats(R, s, t):
    '''
    Input:  R | a list of route tuples
            s | string name of origin city
            t | string name of destination city
    Output: w | maximum weight shippable from s to t
            c | minimum cost to ship weight w from s to t
    '''
    w, c = 0, 0
    
    # cover all cities for dijkstra do not break 
    source_cities = [v[0] for v in R]
    target_cities = [v[1] for v in R]
    all_cities = set(source_cities + target_cities)

    Gw = {v[0]: {} for v in all_cities}
    for s, t, capacity, _ in R:
        Gw[s][t] = capacity
    printG(Gw)


    s = 'E'
    t = 'C'

    # Get the maximum bottleneck, considering the bottlenecks of each path 
    capacities = dijkstra_bottleneck(Gw, s)
    print(capacities)

    wstar = capacities[t]

    Gc = {v[0]: {} for v in all_cities}
    for s, t, capacity, cost in R:
        if capacity < wstar:
            Gc[s][t] = float('inf')
        else:
            Gc[s][t] = cost
    printG(Gc)

    s = 'E'
    t = 'C'
    d, _ = dijkstra(Gc, s)

    print(d)
    cost_result = d[t]
        return w, c
        
    def printG(G):
        print('\n\nGraph:')
        for k, v in G.items():
            print(k, v)
        print('\n\n')




# Construct the graph

R = [('A', 'B', 16, 9), ('A', 'C', 13, 9), ('C', 'D', 23, 24), ('E', 'D', 14, 23), ('C', 'E', 21, 16), ('C', 'A', 12, 18), ('C', 'B', 11, 23), ('E', 'A', 24, 22), ('D', 'A', 3, 25)]

# cover all cities for dijkstra do not break 
source_cities = [v[0] for v in R]
target_cities = [v[1] for v in R]
all_cities = set(source_cities + target_cities)

Gw = {v[0]: {} for v in all_cities}
for s, t, capacity, _ in R:
    Gw[s][t] = capacity
printG(Gw)


s = 'E'
t = 'C'

# Get the maximum bottleneck, considering the bottlenecks of each path 
capacities = dijkstra_bottleneck(Gw, s)
print(capacities)

wstar = capacities[t]

Gc = {v[0]: {} for v in all_cities}
for s, t, capacity, cost in R:
    if capacity < wstar:
        Gc[s][t] = float('inf')
    else:
        Gc[s][t] = cost
printG(Gc)

s = 'E'
t = 'C'
d, _ = dijkstra(Gc, s)

print(d)
cost_result = d[t]
# solves simple reachability problem, to know which of the 
ief try_to_relax_bottleneck(Adj, d, u, v, s):
    # initially all possible capacities are understimates to be 0
    # similar to in a path, in which we are initially pessimit about not being able to reach t from s, that is, set them to +inf distance

    # the relaxation process will check what is the maximum 
    # maximum bottleneck to node v was this d[v]
    # now let's check if reaching v from u we get a larger value

    minimum_capacity_from_u_to_v = min(d[u], w(Adj, u, v))
    # if reaching v from u is less than the value before, we keep the old one
    # if reaching v from u is more than the value before, we update
    old_d = d[v]
    if d[v] < minimum_capacity_from_u_to_v:
        print(f'\nFrom {u} to {v}')
        print(f'New max bottleneck found, because ')
        print(f'{minimum_capacity_from_u_to_v} > {d[v]}')
        print(f'Better to come to {v} from the {u} vertex, since the bottleneck of this new path is larger than the bottleneck of the old path to reach v')
        d[v] = max(d[v], minimum_capacity_from_u_to_v)
        print(f'capacity from {s} to {v} updated from {old_d} to {d[v]}')
    else:
        print('ELSE CLAUSE')
        print(f'New bottleneck is less than the old bottleneck: {minimum_capacity_from_u_to_v} < {d[v]}')

def w(Adj, u, v):
    return Adj[u][v]

def dijkstra_bottleneck(Adj, s):
    '''
    Adj: Adjacency set with weights
    s: source vertex
    '''
    # initial possible weights to be carried from d to other vertices
    d = {v: 0 for v in Adj}
    # full capacity, perfectly possible to carry the object to the same location
    d[s] = float('inf')
    # Initialize the Priority Queue 
    # If in the distance problem the priority is given to the shortest distance vertex coming from s 
    # now the priority is about the maximum bottleneck considering all possible weight of trucks to be carried? - let's call it capacity
    Q = PriorityQueueMaxHeap()
    # Build the PriorityQueue with the vertex and the distance to the source
    for v in Adj:
        Q.insert(v, d[v])
    # Main loop to construct the capacities, that is, the maximum bottlenecks to reach of the vertices from s
    for _ in range(len(Adj)):
        # Extract vertex with maximum capacity to continue the relaxation process to find the maximum bottleneck
        print(f'\n Current Priority Queue')
        print(Q)
        u = Q.extract_max()
        print(f'Extracted vertex to explore frontier {u}')
        # Iterate over each adjancent vertex to the minimun distance vertex
        for v in Adj[u]:
            # try to relax for each adjancet vertex
            try_to_relax_bottleneck(Adj, d, u, v, s)
            # modify the adjancent vertex distance to the source, as the d object was updated in the relaxation process
            Q.decrease_key(v, d[v])
    return d
 can be removed, since from the source vertex we can not get to them
# d, parent = dijkstra(G, s)
# print(d)
# print(parent)

# dag_relaxation(R, s)