
def ao_star(node):
    print(f"Expanding: {node}")

    # Leaf node
    if not graph[node]:
        solved[node] = True
        return heuristic[node]

    best_cost = float('inf')

    for child, ctype in graph[node]:
        if ctype == 'LEAF':
            cost = heuristic[child]
        elif ctype == 'AND':
            # Add all child costs
            cost = 0
            for subchild, _ in graph[child]:
                cost += heuristic[subchild]
        else:
            cost = heuristic[child]

        if cost < best_cost:
            best_cost = cost
            best_child = child
            best_type = ctype

    heuristic[node] = best_cost
    solved[node] = True

    # Go deeper if it's an AND node
    if best_type == 'AND':
        ao_star(best_child)

    return heuristic[node]

# -------- User Input --------
graph = {}
heuristic = {}
solved = {}

n = int(input("How many nodes? "))

print("\nEnter node with children and type (e.g. A B AND C LEAF):")
for _ in range(n):
    parts = input().split()
    node = parts[0]
    children = []
    i = 1
    while i < len(parts):
        child = parts[i]
        ctype = parts[i + 1]
        children.append((child, ctype))
        i += 2
    graph[node] = children

print("\nEnter heuristic values (e.g. A 9):")
for _ in range(n):
    node, value = input().split()
    heuristic[node] = int(value)

start = input("\nEnter start node: ")

# -------- Run AO* --------
final_cost = ao_star(start)
print(f"\nBest path cost from {start}: {final_cost}")
