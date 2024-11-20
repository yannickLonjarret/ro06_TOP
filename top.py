import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import random
import copy

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename



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

###############################

def extract_data_as_numbers(file_path):
    """
    Extracts every line of data from a text file, parsing each value as an integer or float.

    Parameters:
        file_path (str): Path to the file.

    Returns:
        list: A list of lists, where each inner list contains numbers from a line in the file.
    """
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:  # Ignore empty lines
                    # Split by whitespace and convert to float or int
                    numbers = []
                    for value in stripped_line.split():
                        try:
                            num = float(value)
                            num = int(num) if num.is_integer() else num
                            numbers.append(num)
                        except ValueError:
                            pass  # Skip non-numeric values
                    if numbers:
                        data.append(numbers)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def initialize_graph_nodes(parsed_data: list):
    global n,m,L
    n = parsed_data[0][0]
    m = parsed_data[1][0]
    L = parsed_data[2][0]
    for i in range (n):
        G.add_node(i, x=parsed_data[i+3][0], y=parsed_data[i+3][1], profit=parsed_data[i+3][2])
   

def initialize_graph_edges():
    for i in range(n): #0 = d et n+1=a

        for j in range(0,n):
            if i != j:
                
                first_x = G.nodes[i]['x']
                first_y = G.nodes[i]['y']
                second_x = G.nodes[j]['x']
                second_y = G.nodes[j]['y']
                local_cost = (second_x - first_x)**2 + (second_y - first_y)**2
                local_cost = np.sqrt(local_cost)
                local_cost = float(local_cost)
                C.append((i,j, local_cost))

    G.add_weighted_edges_from(C)

def initialize_graph_from_file(filepath):
    parsed_data = extract_data_as_numbers(filepath)
    initialize_graph_nodes(parsed_data)
    initialize_graph_edges()


def initial_routes_creation(R):
    current_computed_route = []
    voisins = list(G.adj[d])


    for i in range(len(voisins)-1):
        current_computed_route.append(d)
        current_computed_route.append(voisins[i])
        current_computed_route.append(n-1)
        deep_copy = copy.deepcopy(current_computed_route)
        R.append(deep_copy)
        current_computed_route.clear()

def compute_savings(all_nodes):
    for i in range(1,len(all_nodes)):
        for j in range(1,len(all_nodes)):
            if i != j:
                
                savingIJ = G.edges[i, n-1]['weight'] + G.edges[0, j]['weight'] - G.edges[i, j]['weight']
                savings.append([i, j, savingIJ])


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

    if(route_1[position1 + 1] != n-1  or route_2[position2 -1]!=d):
        return
    
    merge_route = copy.deepcopy(route_1)
    merge_route.remove(n-1)
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
 

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

initialize_graph_from_file(filename)
# ###########################
initial_routes_creation(R)

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

nx.draw(G, with_labels=True)
plt.show()

