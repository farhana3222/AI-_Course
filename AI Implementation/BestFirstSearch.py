import heapq  # For priority queue (min-heap)

# Function for Best First Search
def best_first_search(graph, heuristic, start, goal):
    
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))  # (heuristic_value, node)
    visited = set()
    traversal_path = []  # To store the path of nodes traversed

    while open_list:
        # Pop the node with the smallest heuristic value
        _, current = heapq.heappop(open_list)
        traversal_path.append(current)  # Add current node to traversal path

        # If the current node is the goal, return the path
        if current == goal:
            return f"Goal {goal} found! Traversal Path: {traversal_path}"

        # Mark the current node as visited
        if current not in visited:
            visited.add(current)

            # Add the neighbors of the current node to the open list
            for neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return f"Goal not found. Traversal Path: {traversal_path}"

# -------- Taking input from user --------
graph = {}
heuristic = {}

# Input the number of nodes
n = int(input("How many nodes are in the graph: "))

# Input graph structure
for _ in range(n):
    node_info = input("Enter a node and its neighbors: ").split()
    node = node_info[0]
    neighbors = node_info[1:] if len(node_info) > 1 else []
    graph[node] = neighbors

# Input heuristic values
for node in graph:
    h_value = int(input(f"Enter the heuristic value for node {node}: "))
    heuristic[node] = h_value

# Input the start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# -------- Run Best First Search --------
result = best_first_search(graph, heuristic, start_node, goal_node)

print(result)
