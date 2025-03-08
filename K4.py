import networkx as nx
import matplotlib.pyplot as plt
import math


# Complete graph generator

node_count = 4

nodes = []

for i in range(1, node_count + 1):
    nodes.append(i)

edges = []

for i in range(1, node_count + 1):
    for j in range(1, node_count + 1):
        if i == j:
            continue
        if not((i,j) in edges or (j,i) in edges):
            edges.append((i, j))

labels = {}

for i in range(1, node_count + 1):
    labels[i] = i

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

plt.figure(figsize=(9, 9))
nx.draw(G, with_labels=True, labels=labels, node_color='black', edge_color='gray', node_size=1000, font_size=16, font_color='white')
plt.show()
