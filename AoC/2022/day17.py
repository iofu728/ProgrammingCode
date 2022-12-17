from collections import defaultdict

g = {-1: [1] * 7}

fig1 = "####"
fig2 = '''.#.
###
.#.'''.split("\n")
fig3 = '''###
..#
..#'''.split("\n")

type1 = [[1] * 4 for ii in range(1)]
type2 = [[int(fig2[ii][jj] == "#") for jj in range(3)] for ii in range(3)]
type3 = [[int(fig3[ii][jj] == "#") for jj in range(3)] for ii in range(3)]
type4 = [[1] for ii in range(4)]
type5 = [[1] * 2 for ii in range(2)]
types = [type1, type2, type3, type4, type5]
types_length = [[len(ii), len(ii[0])] for ii in types]
now_max = -1

with open("day17.txt") as f:
    data = [ii.strip() for ii in f.readlines()]
data = data[0]
idx1, idx2 = 0, 0
N, M = len(types), len(data)

def is_ok(bx, by):
    for ii in range(n):
        for jj in range(m):
            x = bx + ii
            y = by + jj
            if x not in g:
                g[x] = [0] * 7
            if types[i1][ii][jj] == 1 and g[x][y] == 1:
                return False
    return True

cache = {}
WIDTH = 1000000000000 # 2022
def check_cache(idx1, idx2):
    height = now_max
    key = (idx1 % N, idx2 % M)
    if key in cache:
        pre1, pre2 = cache[key]
        if (int(WIDTH) - idx1) % (idx1 - pre1) == 0:
            return height + ((WIDTH - idx1) // (idx1 - pre1)) * (height - pre2)
    else:
        cache[key] = (idx1, height)

while not (answer := check_cache(idx1, idx2)):
    i1, i2 = idx1 % N, idx2 % M
    bx, by = now_max + 4, 2
    sx, sy = bx, by
    n, m = types_length[i1]
    while True:
        i2 = idx2 % M
        d = 1 if data[i2] == ">" else -1
        if by + m + d - 1 < 7 and by + d >= 0:
            by += d
            if not is_ok(bx, by):
                by -= d
        bx -= 1
        if not is_ok(bx, by):
            bx += 1
            break
        # print(bx, by)
        idx2 += 1
    for ii in range(n):
        for jj in range(m):
            x = bx + ii
            y = by + jj
            if x not in g:
                g[x] = [0] * 7
            if types[i1][ii][jj] == 1:
                g[x][y] = 1
                now_max = max(x, now_max)
    idx1 += 1
    idx2 += 1
    # print(bx, by, now_max, g)
    if idx2 % M == 0:
        break
print(answer + 1)