
# coding: utf-8

# In[28]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as ny
from networkx.algorithms import community

'''
node 34 = the administrator
node 1 = the instructor
'''
print('Graph H: Original graph')
H=nx.read_graphml("problem1-ZacharysKarateClub.graphml")
print(nx.info(H))
nx.draw_circular(H, with_labels=True,weight=True)
plt.show()
plt.close()
print('============')

# partition the network into clusters using kernighan_lin_bisection
'''
The input to the algorithm is an undirected graph G = (V,E) with vertex set V, edge set E, and (optionally) 
numerical weights on the edges in E. The goal of the algorithm is to partition V into two disjoint subsets 
A and B of equal (or nearly equal) size, in a way that minimizes the sum T of the weights of the subset of 
edges that cross from A to B. If the graph is unweighted, then instead the goal is to minimize the number 
of crossing edges; this is equivalent to assigning weight one to each edge.
'''
(set1,set2)=community.kernighan_lin_bisection(H, partition=None, max_iter=40, weight='weight')
H1 = H.subgraph(set1)  # create a subgraph with notes in set1
H2 = H.subgraph(set2)  # create a subgraph with notes in set2

print ('set1')
print(set1)
print(nx.info(H1))
nx.draw(H1, with_labels=True,weight=True)
plt.show()
plt.close()
print('============')

print('set2')
print(set2)
print(nx.info(H2))
nx.draw(H2, with_labels=True,weight=True)
plt.show()
plt.close()  

# girvan_newman algorithm: girvan_newman(G, most_valuable_edge=None)
'''
Parameters:
1) G (NetworkX graph)
2) most_valuable_edge (function) – Function that takes a graph as input and outputs an edge. 
The edge returned by this function will be recomputed and removed at each iteration of the algorithm.
If not specified, the edge with the highest networkx.edge_betweenness_centrality() will be used
'''
communities_generator = community.girvan_newman(H)
i=0
for c in next(communities_generator):
    i+=1
    print("Using girvan_newman algorithm: girvan_newman(G, most_valuable_edge=None)")
    print("Level ", i)
    print(c)
    G = H.subgraph(c)
    print(nx.info(G))
    print('')
    nx.draw(G, with_labels=True,weight=True)
    plt.show()
    plt.close()

