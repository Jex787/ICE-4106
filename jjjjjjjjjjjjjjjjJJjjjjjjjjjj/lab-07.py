import math
from collections import defaultdict

# ----------- Given Weighted Graph -----------
xij = [[1, 1, 2], [1, 1], [1, 2, 1], [1, 1]]

# ----------- Graph Construction -----------
g = defaultdict(list)
for node, edges in enumerate(xij):
    g[node].extend(edges)

# ----------- Entropy Function -----------
def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

# ----------- Node Weights and Stationary Distribution -----------
wi = [sum(edges) for edges in g.values()]
w = sum(wi) / 2           # total weight / 2
ui = [weight / (2 * w) for weight in wi]   # stationary distribution

# ----------- Edge Probabilities -----------
wij_div_2w = [weight / (2 * w) for edges in g.values() for weight in edges]

# ----------- Entropy Rate Calculation -----------
H_x = entropy(wij_div_2w) - entropy(ui)

# ----------- Output -----------
print('Entropy Rate: %.2f' % H_x)
