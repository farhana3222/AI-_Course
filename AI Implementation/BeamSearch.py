def beam_search(start, tree, beam_width):
    beam = [(tree[start]['value'], start)]  # Start node with its heuristic value
    visited = set()

    while beam:
        next_beam = []

        for cost, node in beam:
            if node in visited:
                continue
            visited.add(node)

            # Add children to next level with their heuristic values
            for child in tree[node]['children']:
                next_beam.append((tree[child]['value'], child))

        if not next_beam:
            break

        # Sort by heuristic value (lowest is better), then keep top `beam_width`
        next_beam.sort(key=lambda x: x[0])
        beam = next_beam[:beam_width]

    return beam


# ------------ USER INPUT PART ------------
tree = {}
n = int(input("How many nodes? "))

print("\nEnter each node with its children and heuristic value:")
for _ in range(n):
    parts = input("Format: Node Child1 Child2 ... HeuristicValue => ").split()
    node = parts[0]
    *children, value = parts[1:]
    tree[node] = {
        'children': children,
        'value': int(value)
    }

start_node = input("Enter the start node: ")
beam_width = int(input("Enter the beam width: "))

# ------------ RUN BEAM SEARCH ------------
result = beam_search(start_node, tree, beam_width)

# ------------ OUTPUT ------------
print("\nFinal Beam (last explored nodes):")
for cost, node in result:
    print(f"Node {node} with heuristic {cost}")
