# import networkx as nx
# import matplotlib.pyplot as plt

# # Define the directed graph
# graph = {
#     1: {2: 50, 4: 10, 3: 45},
#     2: {3: 10, 4: 15},
#     3: {5: 30},
#     4: {1: 10, 5: 15},
#     5: {3: 35},
#     6: {5: 1}
# }

# # Convert the graph into a directed graph
# G = nx.DiGraph(graph)

# # Plot the directed graph
# pos = nx.spring_layout(G)  # Position nodes using the spring layout algorithm
# nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold', arrows=True)

# # Draw edge labels with weights
# edge_labels = {(u, v): G[u][v] for u, v in G.edges()}
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', label_pos=0.5)

# # Display the graph
# plt.title('Directed Graph with Edge Weights')
# plt.show()



import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
graph = {
    1: {2: 50, 4: 10, 3: 45},
    2: {3: 10, 4: 15},
    3: {5: 30},
    4: {1: 10, 5: 15},
    5: {3: 35},
    6: {5: 1}
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph with their edge labels (weights)
for source, targets in graph.items():
    for target, weight in targets.items():
        G.add_edge(source, target, weight=weight)

# Draw the graph with edge labels as weights
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the graph
plt.title("Directed Graph with Edge Weights")
plt.show()
