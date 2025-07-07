from collections import deque

def bfs_tree(tree, root):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        for child in tree[node]:
            queue.append(child)

# -------- Taking input for tree --------
tree = {}
n = int(input("How many nodes are there: "))

for _ in range(n):
    node_info = input("Enter a node and its children : ").split()
    node = node_info[0]
    children = node_info[1:] if len(node_info) > 1 else []
    tree[node] = children

root = input("root node: ")

# -------- Running BFS --------
print("BFS Traversal of Tree:")
bfs_tree(tree, root)
