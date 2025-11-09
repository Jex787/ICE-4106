message = 'AABABBBABAABABBBABBABB'
# ----------- Build dictionary -----------
dictionary = {}
tmp, i, last = '', 1, 0

for x in message:
    tmp += x
    if tmp not in dictionary:
        dictionary[tmp] = i
        tmp = ''
        i += 1
    else:
        last = dictionary[tmp]
# ----------- Build output list -----------
res = ['1']  # first entry
for char, idx in list(dictionary.items())[1:]:
    tmp = ''
    s = ''
    for j, x in enumerate(char[:-1]):
        tmp += x
        if tmp in dictionary:
            take = dictionary[tmp]
            s = str(take) + char[j + 1:]
    if len(char) == 1:
        s = char
    res.append(s)

# Append last index if needed
if last:
    res.append(str(last))
# ----------- Binary conversion -----------
mark = {'A': 0, 'B': 1}
final_res = []
for x in res:
    tmp = ''
    for c in x:
        tmp += str(mark[c]) if c.isalpha() else bin(int(c))[2:]
    final_res.append(tmp.zfill(4))
# ----------- Output -----------
print(res)
print("Encoded:", final_res)
