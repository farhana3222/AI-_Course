def a_star(graph, heuristic, start, goal):
    open_list = [start]
    g_score = {start: 0}
    parent = {start: None}

    while open_list:
        # Choose node with lowest f(n) = g(n) + h(n)
        current = min(open_list, key=lambda node: g_score[node] + heuristic[node])
        open_list.remove(current)

        if current == goal:
            path = []
            while current:
                path.insert(0, current)
                current = parent[current]
            return path

        for neighbor, cost in graph.get(current, []):
            new_g = g_score[current] + cost
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                parent[neighbor] = current
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None

# ---------- User Input ----------
graph = {}
heuristic = {}

n = int(input("How many nodes? "))

print("\nEnter neighbors and cost (Example: A B 1 C 2):")
for _ in range(n):
    parts = input().split()
    node = parts[0]
    neighbors = []
    for i in range(1, len(parts), 2):
        neighbors.append((parts[i], int(parts[i+1])))
    graph[node] = neighbors

print("\nEnter heuristic values (Example: A 5):")
for _ in range(n):
    node, h = input().split()
    heuristic[node] = int(h)

start = input("\nStart node: ")
goal = input("Goal node: ")

# ---------- Run A* ----------
path = a_star(graph, heuristic, start, goal)

# ---------- Output ----------
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")
