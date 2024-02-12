import networkx as nx
import matplotlib.pyplot as plt

# Create the graph
graph = {'s': {'a': 2, 'b': 1},
         'a': {'s': 3, 'b': 4, 'c': 8},
         'b': {'s': 4, 'a': 2, 'd': 2},
         'c': {'a': 2, 'd': 7, 't': 4},
         'd': {'b': 1, 'c': 11, 't': 5},
         't': {'c': 3, 'd': 5}}

# Create a directed graph from the given graph
G = nx.DiGraph()

# Add nodes and edges with weights
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Plot the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)
edge_labels = {(i, j): w.get('weight', 1) for i, j, w in G.edges(data=True)}  # Extract edge weights, default to 1 if 'weight' attribute not found
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title('Graph Plot')
plt.show()
