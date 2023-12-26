import matplotlib.pyplot as plt
import networkx as nx

# Define the adjacency list for the DAG
Adj = {
    '19.854': {},  # Target course with prerequisites from level 4
    '101': {}, '102': {}, '103': {}, '104': {}, '105': {},
    '201': {'101': 2}, '202': {'102': 2}, '203': {'103': 3}, '204': {'104': 1}, '205': {'105': 4},
    '301': {'201': 2, '202': 1}, '302': {'202': 3}, '303': {'203': 2}, '304': {'204': 4}, '305': {'205': 3},
    '401': {'301': 5, '302': 2}, '402': {'302': 3, '303': 2}, '403': {'303': 4, '304': 1},
    '404': {'304': 3}, '405': {'305': 2},
    '501': {'401': 2, '402': 1}, '502': {'402': 3, '403': 2}, '503': {'403': 3}, '504': {'404': 4},
    '505': {'405': 1}, '19.854': {'501': 3, '502': 4, '503': 2, '504': 5, '505': 1}
}

# Create a directed graph from the adjacency list
G = nx.DiGraph()
for node, edges in Adj.items():
    for target, weight in edges.items():
        G.add_edge(node, target, weight=weight)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=10)
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title('Directed Acyclic Graph for Course Prerequisites')
plt.show()

