import heapq, math
from collections import Counter

def calculate_frequency(text):
    return dict(Counter(text.upper().replace(' ', '')))

def build_huffman_tree(freq):
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0]+hi[0]] + lo[1:] + hi[1:])
    return heap[0]

def huffman_avg_length(freq, tree, length):
    return sum(len(pair[1]) * (freq[pair[0]]/length) for pair in tree[1:])

def entropy(freq, length):
    return -sum((f/length) * math.log2(f/length) for f in freq.values())

# ----------- Example Usage -----------
message = "aaabbbbbccccccddddee"
freq = calculate_frequency(message)
tree = build_huffman_tree(freq)

huff_len = huffman_avg_length(freq, tree, len(message))
H = entropy(freq, len(message))

print(f"Huffman: {huff_len:.2f} bits")
print(f"Entropy: {H:.2f} bits")
print("Huffman code is optimal" if huff_len >= H else "Code is not optimal")
