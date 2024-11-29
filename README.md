# **Naive Team Orienteering Problem (TOP) solution using Clarke and Wright Algorithm**

This project implements a solution to the **TOP** using the **Savings Algorithm**. The objective is to optimize routes for vehicles visiting multiple customers, maximizing profits under given constraints.

The program utilizes **NetworkX** for graph representation, **NumPy** for calculations, and **Matplotlib** for visualizations. It also features an interactive file loader for importing customer and vehicle data.

This was developed as part of a programming assignment for RO06 during the 2024-2025 academic year. The project was created by Mathieu Kozebda and Yannick Lonjarret.

---

## **How It Works**
1. **Input Data**:
   - The program expects a text file containing:
     - The number of customers, vehicles, and maximum route time (`L`).
     - Coordinates (x, y) and profit for each customer.
   - File format example:
     ```
     100    # Number of customers
     100    # Number of vehicles
     1000   # Time limit
     0 0 0  # Depot: x, y, profit
     10 15 20  # Customer 1: x, y, profit
     30 40 50  # Customer 2: x, y, profit
     ```

2. **Graph Initialization**:
   - Nodes are created for customers and the depot, with associated attributes.
   - Edges are created with weights based on Euclidean distances.

3. **Savings Algorithm**:
   - Cost savings for merging routes are calculated for all node pairs.
   - Routes are iteratively merged based on the highest savings while respecting constraints.

4. **Profit Calculation**:
   - Computes the profit for each route and outputs the total global profit.

5. **Visualization**:
   - Displays the graph with nodes and edges to show the computed routes.

---

## **Installation**
### **Dependencies**
Ensure you have the following Python libraries installed:
- `numpy`
- `networkx`
- `matplotlib`
- `tkinter` (included in most Python installations)

You can install missing libraries using pip:
```bash
pip install numpy networkx matplotlib
```

---

## **Usage**
1. Clone the repository:
   ```bash
   git clone https://github.com/yannickLonjarret/ro06_TOP.git
   cd ro06_TOP
   ```

2. Run the program:
   ```bash
   python top.py
   ```

3. Select an input file using the file dialog.

4. View the calculated routes and global profit in the console and the graph visualization window.

---

## **License**
This project is licensed under the MIT License.
