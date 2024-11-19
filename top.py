import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import random
import copy


######Initialisation

V=[]
E=[]

n=10 #nombre de client
L=1000 #limite de temps
m=4 #nombre de véhicules
C_lim=100 #limite de coût d'un arc (modifiable)
P_lim=100 #limite de profit sur un client

C=[] #Arcs avec coût
P=[] #Liste des profits
R=[] #Liste des routes
X=np.zeros(n) #Liste des clients visités

d=0
a=n+1

G=nx.Graph()
for i in range(n+2): #0 = d et n+1=a
    V.append(i)

    for j in range(n+2):
        if i !=j:
            E.append((i,j))
            C.append((i,j, random.randint(1,L)))

for i in range(n):
    P.append(random.randint(0,P_lim))

G.add_weighted_edges_from(C)

def initial_routes_creation():
    current_computed_route = []
    voisins = list(G.adj[d])


    for i in range(len(voisins)-1):
        current_computed_route.append(d)
        current_computed_route.append(voisins[i])
        current_computed_route.append(a)
        deep_copy = copy.deepcopy(current_computed_route)
        R.append(deep_copy)
        current_computed_route.clear()

def compute_savings(all_nodes):
    for i in range(1,len(all_nodes)-1):
        for j in range(1,len(all_nodes)-1):
            if i != j:
                savingIJ = G.edges[i, n+1]['weight'] + G.edges[0, j]['weight'] - G.edges[i, j]['weight']
                if savingIJ >= 0: 
                    savings.append([i, j, savingIJ])

def merge_routes(route_node, node_to_evalutate):
    route_1 = []
    route_2 = []
    for r in R:
        if route_node in r:
            if node_to_evalutate in r:
                return
            route_1 = r
        if node_to_evalutate in r:
            route_2 = r




###########################
initial_routes_creation()
voisins = list(G.adj[d])
savings = []
compute_savings(voisins)
###########################



savings.sort(key=lambda x: x[2], reverse=True)
print(savings)
print(G.edges.data())
#nx.draw(G, with_labels=True)
#plt.show()

