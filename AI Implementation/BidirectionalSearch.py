from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Queues for both searches
    q_start = deque([start])
    q_goal = deque([goal])

    # Visited sets
    visited_start = {start}
    visited_goal = {goal}

    # Parent maps to build path
    parent_start = {start: None}
    parent_goal = {goal: None}

    while q_start and q_goal:
        # Expand from start side
        node_from_start = q_start.popleft()
        for neighbor in graph[node_from_start]:
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                parent_start[neighbor] = node_from_start
                q_start.append(neighbor)
                if neighbor in visited_goal:
                    return build_path(neighbor, parent_start, parent_goal)

        # Expand from goal side
        node_from_goal = q_goal.popleft()
        for neighbor in graph[node_from_goal]:
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                parent_goal[neighbor] = node_from_goal
                q_goal.append(neighbor)
                if neighbor in visited_start:
                    return build_path(neighbor, parent_start, parent_goal)

    return None

def build_path(meeting_node, parent_start, parent_goal):
    path = []

    # From start to meeting point
    node = meeting_node
    while node:
        path.append(node)
        node = parent_start[node]
    path.reverse()

    # From meeting point to goal
    node = parent_goal[meeting_node]
    while node:
        path.append(node)
        node = parent_goal[node]

    return path

# -------- User Input --------
graph = {}
n = int(input("How many nodes? "))

print("Enter each node followed by its neighbors (space separated):")
for _ in range(n):
    parts = input().split()
    node = parts[0]
    neighbors = parts[1:]
    graph[node] = neighbors

start = input("Start node: ")
goal = input("Goal node: ")

# -------- Run Search --------
path = bidirectional_search(graph, start, goal)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")
