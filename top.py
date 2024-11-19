import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import random
import copy


######Initialisation

V=[]
E=[]

n=100 #nombre de client
L=1000 #limite de temps
m=100 #nombre de véhicules
C_lim=250 #limite de coût d'un arc (modifiable)
P_lim=100 #limite de profit sur un client

C=[] #Arcs avec coût
R=[] #Liste des routes
Resulting_Routes=[]
Global_profit = 0
d=0
a=n+1

G=nx.Graph()
for i in range(n+2): #0 = d et n+1=a
    V.append(i)

    for j in range(n+2):
        if i !=j:
            E.append((i,j))
            C.append((i,j, random.randint(125,C_lim)))

G.add_node(d, profit=0) #profit au dépôt d
for i in range(1,n+1):
    G.add_node(i, profit=random.randint(10,P_lim))
G.add_node(a, profit=0) #profit au dépôt a

G.add_weighted_edges_from(C)
###############################

def initial_routes_creation(R):
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
    for i in range(1,len(all_nodes)):
        for j in range(1,len(all_nodes)):
            if i != j:
                savingIJ = G.edges[i, n+1]['weight'] + G.edges[0, j]['weight'] - G.edges[i, j]['weight']
                savings.append([i, j, savingIJ])


def calc_profits(P,X):
    profits=0
    for i in range (len(P)):
        profits=profits+X[i]*P[i]
    
    return profits


def compute_single_route_profit(route):
    profits = 0

    for i in route:
        profits = profits + G.nodes[i]['profit']
    return profits

def compute_all_route_profit():
    profits = []

    for r in R:
        profits.append(compute_single_route_profit(r))
    
    return profits

def compute_global_profit(route_profits: list):
    global_profit = 0
    for i in range(m):
        local_max = max(route_profits)
        global_profit +=  local_max
        index = route_profits.index(local_max)

        Resulting_Routes.append(R[index])
        route_profits[index] = 0
    return global_profit

def clear_empty_route():
    i = 0
    while i < len(R):
        if R[i][:] == []:
            R.pop(i)
        else:
            i = i+1



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

    position1 = route_1.index(route_node)
    position2 = route_2.index(node_to_evalutate)

    if(route_1[position1 + 1] != a  or route_2[position2 -1]!=d):
        return
    
    merge_route = copy.deepcopy(route_1)
    merge_route.remove(a)
    for i in range(1, len(route_2)):
        merge_route.append(route_2[i])

    cost = 0
    for i in range(len(merge_route) - 1):
        val = int(G.edges[merge_route[i], merge_route[i+1]]['weight'])
        cost = cost + val
    if cost > L:
        return
    route_2.clear()
    
    for i,r in enumerate(R):
        if r == route_1:
            R[i] = merge_route


    




###########################
initial_routes_creation(R)
print("Routes :", R)
voisins = list(G.adj[d])
savings = []
compute_savings(voisins)

###########################
savings.sort(key=lambda x: x[2], reverse=True)
for i in range(len(savings)):
    merge_routes(list(G.nodes)[savings[i][0]], list(G.nodes)[savings[i][1]])


pr = compute_all_route_profit()
Global_profit = compute_global_profit(pr)
print(Resulting_Routes)
print(Global_profit)
#print("Savings : ",savings)
#print(G.edges.data())
#print(G.nodes.data())
nx.draw(G, with_labels=True)
#plt.show()

