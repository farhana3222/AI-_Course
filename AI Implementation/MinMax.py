class Node:
    def __init__(self, value=None, children=None):
        self.value = value  # For leaf nodes
        self.children = children if children else []

def minimax(node, is_maximizing):
    if not node.children:  # Leaf node
        return node.value

    if is_maximizing:
        return max(minimax(child, False) for child in node.children)
    else:
        return min(minimax(child, True) for child in node.children)

# Take user input
print("Building a simple tree with 4 leaf nodes...")

leaf_values = []
for i in range(4):
    val = int(input(f"Enter value for leaf {i + 1}: "))
    leaf_values.append(Node(value=val))

# Create internal nodes assuming two MIN nodes each with two children
min1 = Node(children=[leaf_values[0], leaf_values[1]])
min2 = Node(children=[leaf_values[2], leaf_values[3]])

# Create MAX root
root = Node(children=[min1, min2])

# Run minimax
result = minimax(root, is_maximizing=True)
print("Minimax result:", result)
