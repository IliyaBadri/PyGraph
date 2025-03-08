import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Complete graph generator
node_count = 64

nodes = list(range(1, node_count + 1))
edges = [(i, j) for i in nodes for j in nodes if i < j]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

edge_colors = plt.cm.rainbow(np.linspace(0, 1, len(edges)))

plt.figure(figsize=(9, 9))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='black',
    edge_color=edge_colors,
    edge_cmap=plt.cm.rainbow,
    node_size=1000,
    font_size=16,
    font_color='white'
)

plt.show()
