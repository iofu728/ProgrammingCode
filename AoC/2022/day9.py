with open("day9.txt") as f:
    data = [ii.strip().split() for ii in f.readlines()]



res = set()
DIRS = {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}

def change(x1, y1, x2, y2):
    if x1 == x2 and abs(y1 - y2) == 2:
        return x2, (y1 + y2) // 2
    if y1 == y2 and abs(x1 - x2) == 2:
        return (x1 + x2) // 2, y2
    if x1 != x2 and y1 != y2 and not (abs(x1 - x2) == 1 and abs(y1 - y2) == 1):
        dx = -1 if x1 < x2 else 1
        dy = -1 if y1 < y2 else 1
        return x2 + dx, y2 + dy
    return x2, y2

x1, y1 = 0, 0
x2, y2 = 0, 0
res.add((x2, y2))
for ii, jj in data:
    jj = int(jj)
    for _ in range(jj):
        dx, dy = DIRS[ii]
        x1, y1 = x1 + dx, y1 + dy
        x2, y2 = change(x1, y1, x2, y2)
        # print(x1, y1, x2, y2)
        res.add((x2, y2))



xs = [(0, 0) for ii in range(10)]
res.add(xs[-1])
for ii, jj in data:
    jj = int(jj)
    for _ in range(jj):
        dx, dy = DIRS[ii]
        xs[0] = xs[0][0] + dx, xs[0][1] + dy
        for kk in range(9):
            xs[kk + 1] = change(*xs[kk], *xs[kk + 1])
        # print(x1, y1, x2, y2)
        res.add(xs[-1])
