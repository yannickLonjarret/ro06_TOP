import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import random



######Initialisation

V=[]
E=[]

n=10 #nombre de client
L=100 #limite de temps
m=4 #nombre de véhicules
C_lim=L #limite de coût d'un arc (modifiable)
P_lim=100 #limite de profit sur un client

C=[] #matrice des coûts
P=[] #matrice des profits

d=0
a=n+1

G=nx.Graph()
for i in range(n+2): #0 = d et n+1=a
    V.append(i)
    P.append(random.randint(0,P_lim))
    for j in range(n+2):
        if i !=j:
            E.append((i,j))
            C.append((i,j, random.randint(1,L)))

G.add_weighted_edges_from(C)

####################

print(C)
nx.draw(G, with_labels=True)
plt.show()

