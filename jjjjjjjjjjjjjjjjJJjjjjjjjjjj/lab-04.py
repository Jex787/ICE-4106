import math

# Given symmetric channel matrix
matrix = [[2/3, 1/3], [1/3, 2/3]]

print("Symmetric matrix is:")
for i in range(2):
    for j in range(2):
        print('%.2f' % matrix[i][j], end='  ')
    print()

# Calculate H(Y|X) using formula (1-p)log(1/(1-p)) + plog(1/p)
# For symmetric channel, H(Y|X) is the same for all inputs
H_y_given_x = matrix[0][0] * math.log2(1.0 / matrix[0][0]) + matrix[0][1] * math.log2(1.0 / matrix[0][1])

print("Conditional entropy H(Y|X) is = %.3f" % H_y_given_x, "bits/msg symbol")

# Calculate channel capacity using formula C = 1 - H(Y|X)
# For binary symmetric channel with uniform input distribution
channel_capacity = 1 - H_y_given_x

print("Channel Capacity is = %.3f" % channel_capacity, "bits/msg symbol")