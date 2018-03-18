
# coding: utf-8

# In[97]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as ny

'''
node 34 = the administrator
node 1 = the instructor
'''
print('Graph H: Original graph')
H=nx.read_graphml("problem1-ZacharysKarateClub.graphml")
degree = nx.degree(H) # degree centrality
print('degrees =',degree)
node_list = [n for (n,m) in degree]
degree_list = [int(m) for (n, m) in degree]
print('node type =',type(node_list[0]))
print('nodes = ', node_list)
print('degree type =',type(degree_list[0]))
print('degrees =',degree_list)
print('============')
'''
d = nx.degree(g)  # d is not a dictionary type, but a report view.
nx.draw(g, nodelist=d.keys(), node_size=[v * 100 for v in d.values()])  # this didn't work
'''
print('Draw node proportion to the degree of the node')
print(nx.info(H))
nx.draw_kamada_kawai(H, with_labels=True,nodelist=node_list,node_size=[n*70 for n in degree_list])
plt.show()
plt.close()

