with open("day3.txt") as f:
    data = [ii.strip() for ii in f.readlines()]

def get_score(x):
    if x.isupper():
        return ord(x) - 64 + 26
    return ord(x) - 96

res = 0
for line in data:
    N = len(line) // 2
    b = set(line[N:])
    idx = set([ii for ii in line[:N] if ii in b])
    for ii in idx:
        res += get_score(ii)


res = 0
for idx in range(0, len(data), 3):
    a, b, c = data[idx:idx + 3]
    a, b, c = set(a), set(b), set(c)
    idx = set([ii for ii in a if ii in b and ii in c])
    for ii in idx:
        res += get_score(ii)
