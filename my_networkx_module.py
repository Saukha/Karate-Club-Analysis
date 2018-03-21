
# coding: utf-8

# In[70]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as ny
from networkx.algorithms import community
from operator import itemgetter

#print nodes sorted by degree centrality in decending order
def print_nodes_by_degree_cent (g, x=all):
    degree_centrality_dict = nx.degree_centrality(H) # calculate degree centrality for each node
    sorted_degree = sorted(degree_centrality_dict.items(), key=itemgetter(1), reverse=True) #sort in reverse
    print("Nodes sorted by degree centrality:")
    if x==all:
        for b in sorted_degree[:]: #print all nodes with degree centrality
            print(b) 
    else:
        for b in sorted_degree[:x]: #print top x nodes with degree centrality
            print(b) 

#print nodes sorted by betweenness centrality in decending order
def print_nodes_by_betweenness_cent (g, x=all): #input g=graph; x=number of nodes
    betweenness_centrality_dict = nx.betweenness_centrality(H) # calculate betweenness centrality for each node
    sorted_betweenness = sorted(betweenness_centrality_dict.items(), key=itemgetter(1), reverse=True) #sort in reverse
    print("Nodes sorted by betweenness centrality:")
    if x==all:
        for b in sorted_betweenness[:]: #print all nodes with betweenness centrality
            print(b) 
    else:
        for b in sorted_betweenness[:x]: #print top x nodes with betweenness centrality
            print(b) 

#print nodes sorted by closeness centrality in decending order
def print_nodes_by_closeness_cent (g, x=all): #input g=graph; x=number of nodes
    closeness_centrality_dict = nx.closeness_centrality(H) # closeness centrality for each node
    sorted_closeness = sorted(closeness_centrality_dict.items(), key=itemgetter(1), reverse=True) #sort in reverse
    print("Nodes sorted by closeness centrality:")
    if x==all:
        for b in sorted_closeness[:]: #print all nodes with closeness centrality
            print(b) 
    else:
        for b in sorted_closeness[:x]: #print top x nodes with closeness centrality
            print(b)

#print nodes sorted by eigenvector centrality in decending order
def print_nodes_by_eigenvector_cent (g, x=all): #input g=graph; x=number of nodes
    eigenvector_centrality_dict = nx.eigenvector_centrality(H)  # eigenvactor centrality for each node
    sorted_eigenvector = sorted(eigenvector_centrality_dict.items(), key=itemgetter(1), reverse=True) #sort in reverse
    print("Nodes sorted by eigenvector centrality:")
    if x==all:
        for b in sorted_eigenvector[:]: #print all nodes with eigenvector centrality
            print(b) 
    else:
        for b in sorted_eigenvector[:x]: #print top x nodes with eigenvector centrality
            print(b)

#print nodes sorted by page rank centrality in decending order
def print_nodes_by_page_rank_cent (g, x=all): #input g=graph; x=number of nodes
    page_rank_centrality_dict = nx.pagerank(H) # page rank centrality for each node
    sorted_page_rank = sorted(page_rank_centrality_dict.items(), key=itemgetter(1), reverse=True) #sort in reverse
    print("Nodes sorted by page rank centrality:")
    if x==all:
        for b in sorted_page_rank[:]: #print all nodes with page rank centrality
            print(b) 
    else:
        for b in sorted_page_rank[:x]: #print top x nodes with page rank centrality
            print(b)

# draw node proportion to the degree of the node
def draw_node_size_by_deg (g, scale=None, with_labels=True): 
    degree = nx.degree(g) # degree centrality
    node_list = [n for (n,m) in degree]
    degree_list = [int(m) for (n, m) in degree]  
    if scale==None:
        nx.draw_kamada_kawai(g, with_labels=with_labels,nodelist=node_list,node_size=[n*70 for n in degree_list])
    else:        
        nx.draw_kamada_kawai(g, with_labels=with_labels,nodelist=node_list,node_size=[n*scale for n in degree_list])
    plt.show()
    plt.close()

# print network/graph info    
def print_graph_info(g):
    print (nx.info(g))
    print ("Network diameter = ", nx.diameter(g))
    print ("Network average clustering coefficient = ", nx.average_clustering(g))
    print ("Network density = ", nx.density(g))
    print ("Network average shortest path length= ",nx.average_shortest_path_length(g))



