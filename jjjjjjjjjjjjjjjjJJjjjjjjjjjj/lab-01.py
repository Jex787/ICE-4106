def encode(msg, K, n):
    # Input generator polynomials
    gens = [list(map(int, input(f'Enter bits for generator {i}: ').split())) for i in range(n)]

    # Convolution (polynomial multiplication mod 2)
    def conv(a, b):
        res = [0] * (len(a) + len(b) - 1)
        for i in range(len(a)):
            for j in range(len(b)):
                res[i + j] ^= a[i] & b[j]
        return res

    # Compute convolution for each generator
    convs = [conv(msg, g) for g in gens]

    # Interleave outputs from all generators
    encoded = [convs[j][i] % 2 for i in range(len(convs[0])) for j in range(n)]
    return encoded

# ---------------- Inputs ----------------
msg = list(map(int, input('Enter message: ').split()))
K = int(input('Constraints: '))
n = int(input('Number of output(generator): '))

# ---------------- Output ----------------
print('Encoded Message:', encode(msg, K, n))
