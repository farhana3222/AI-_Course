def alpha_beta(depth, index, is_max, alpha, beta, values, max_depth):
    if depth == max_depth:
        return values[index]# if reach the leaf then  return current node

    if is_max:
        best = float('-inf') #value is infinity
        for i in range(2): 
            
            val = alpha_beta(depth + 1, index * 2 + i, False, alpha, beta, values, max_depth) #for children index
            best = max(best, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, True, alpha, beta, values, max_depth)
            best = min(best, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return best

# ----------- Input Section -------------
n = int(input("How many leaf values: "))
values = []

for i in range(n):
    val = int(input(f"Enter leaf {i+1}: "))
    values.append(val)

depth = 0
index = 0
is_maximizing = True
alpha = float('-inf')
beta = float('inf')
max_depth = n.bit_length() - 1  # log2(n)

result = alpha_beta(depth, index, is_maximizing, alpha, beta, values, max_depth)
print("Best value:", result)
