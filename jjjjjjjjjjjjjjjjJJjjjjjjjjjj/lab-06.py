import math

# ----------- Given Joint Probability Matrix -----------
matrix = [
    [1/8, 1/16, 1/32, 1/32],
    [1/16, 1/8, 1/32, 1/32],
    [1/16, 1/16, 1/16, 1/16],
    [1/4, 0, 0, 0]
]

# ----------- Entropy Function -----------
def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

# ----------- Marginal Distributions -----------
marginal_x = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
marginal_y = [sum(row) for row in matrix]

# ----------- Conditional Entropies -----------
H_x_given_y = sum(entropy([matrix[i][j]/marginal_y[i] if marginal_y[i]>0 else 0 for j in range(len(matrix[0]))]) * marginal_y[i] for i in range(len(matrix)))
H_y_given_x = sum(entropy([matrix[j][i]/marginal_x[i] if marginal_x[i]>0 else 0 for j in range(len(matrix))]) * marginal_x[i] for i in range(len(matrix[0])))

# ----------- Joint Entropy & Mutual Information -----------
H_x = entropy(marginal_x)
H_y = entropy(marginal_y)
H_xy = H_x + H_y_given_x
I_xy = H_y - H_y_given_x

# ----------- Output -----------
print('Conditional Entropy H(x|y):', H_x_given_y)
print('Conditional Entropy H(y|x):', H_y_given_x)
print('Joint Entropy H(x,y):', H_xy)
print('Mutual Information:', I_xy)
