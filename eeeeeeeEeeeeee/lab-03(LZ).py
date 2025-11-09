def lempel_ziv_encode(data):
    dictionary = {'0': 1, '1': 2}
    next_index = 3
    i = 0
    encoded_pairs = []

    while i < len(data):
        j = i + 1
        while j <= len(data) and data[i:j] in dictionary:
            j += 1
        if j > len(data):
            break
        dictionary[data[i:j]] = next_index
        next_index += 1
        prefix = data[i:j-1]
        next_symbol = data[j-1]
        encoded_pairs.append(str(dictionary[prefix]) + next_symbol)
        i = j - 1
    return encoded_pairs

def to_binary_blocks(encoded_pairs, block_size=4):
    return [("".join(format(int(ch), "b") for ch in pair)).zfill(block_size)
            for pair in encoded_pairs]

# -------- MAIN --------
data = "000101110010100101"
encoded_pairs = lempel_ziv_encode(data)
binary_blocks = to_binary_blocks(encoded_pairs)

print("\nBinary encoded blocks:")
print(binary_blocks)
