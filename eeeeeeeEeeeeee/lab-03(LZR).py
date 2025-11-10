# ===== Lempel–Ziv Code Algorithm =====

data = input("Input: ").strip()
d, out, i = ['0', '1'], [], 0

while i < len(data):
    for j in range(i + 1, len(data) + 1):
        s = data[i:j]
        if s not in d:
            d.append(s)
            p = s[:-1]
            idx = d.index(p) + 1 if p else 0
            out.append(str(idx) + s[-1])
            break
    i = j

print("\nBinary encoded blocks:")
print([(''.join(format(int(c), 'b') for c in p)).zfill(4) for p in out])
