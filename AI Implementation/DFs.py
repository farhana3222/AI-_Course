def dfs_tree(tree, node):
    print(node, end=' ')  # Visit the node

    for child in tree[node]:  # Explore all children
        dfs_tree(tree, child)

# -------- Taking input for tree --------
tree = {}
n = int(input("How many nodes are there: "))

for _ in range(n):
    node_info = input("Enter a node and its children: ").split()
    node = node_info[0]
    children = node_info[1:] if len(node_info) > 1 else []
    tree[node] = children

root = input(" root node: ")

# -------- Running DFS --------
print("DFS Traversal of Tree:")
dfs_tree(tree, root)

