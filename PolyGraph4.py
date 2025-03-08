import networkx as nx
import matplotlib.pyplot as plt
import math


# Complete graph generator

node_count = 4

nodes = []

for i in range(1, node_count + 1):
    nodes.append(i) # [1, 4]
    nodes.append(i+node_count) # [5, 8]
    nodes.append(i+node_count*2) # [9, 12]
    nodes.append(i+node_count*3) # [13, 16]

edges = []

for i in range(1, node_count + 1):
    for j in range(1, node_count + 1):
        if i == j:
            continue

        if not((i,j) in edges or (j,i) in edges):
            edges.append((i, j))

        if not((i+node_count,j+node_count) in edges or (j+node_count,i+node_count) in edges):
            edges.append((i+node_count, j+node_count))
            
        if not((i+node_count*2,j+node_count*2) in edges or (j+node_count*2,i+node_count*2) in edges):
            edges.append((i+node_count*2, j+node_count*2))

        if not((i+node_count*3,j+node_count*3) in edges or (j+node_count*3,i+node_count*3) in edges):
            edges.append((i+node_count*3, j+node_count*3))

edges.append((1, 5))
edges.append((3, 7))

edges.append((6, 10))
edges.append((8, 12))

edges.append((9, 13))
edges.append((11, 15))

edges.append((14, 2))
edges.append((16, 4))



labels = {}

for i in range(1, node_count + 1):
    labels[i] = i
    labels[i+node_count] = i
    labels[i+node_count*2] = i
    labels[i+node_count*3] = i

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos = nx.spring_layout(G)

plt.figure(figsize=(13, 9))
nx.draw(G, pos, with_labels=True, labels=labels, node_color='black', edge_color='gray', node_size=500, font_size=16, font_color='white')
plt.show()
