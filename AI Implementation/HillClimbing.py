# Function for Hill Climbing Search
def hill_climbing_tree(start, tree):
    current = start
    while True:
        # Get the neighbors (children of the current node)
        neighbors = tree[current]['children']
        
        # If there are no children, we are at a leaf node, break
        if not neighbors:
            break
        
        # Find the neighbor with the maximum value (greedy step)
        next_move = max(neighbors, key=lambda x: tree[x]['value'])
        
        # If the next move has a higher value, move there
        if tree[next_move]['value'] > tree[current]['value']:
            current = next_move
        else:
            # If no neighbor has a higher value, stop
            break
    
    return current, tree[current]['value']

# -------- Taking input from user --------
tree = {}

# Input the number of nodes in the tree
n = int(input("How many nodes are in the tree? "))

# Input the tree structure
for _ in range(n):
    node_info = input("Enter a node with its children and heuristic value (space-separated): ").split()
    node = node_info[0]
    children = node_info[1:-1] if len(node_info) > 2 else []
    value = int(node_info[-1])  # heuristic value
    tree[node] = {'children': children, 'value': value}

# Input the start node
start_node = input("Enter the start node: ")

# -------- Run Hill Climbing Search --------
final_node, final_value = hill_climbing_tree(start_node, tree)

print(f"Climbing finished at node {final_node} with value {final_value}.")
