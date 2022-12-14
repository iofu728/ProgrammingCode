from collections import defaultdict
import bisect

with open("day14.txt") as f:
    data = [ii.strip() for ii in f.readlines()]


g = defaultdict(list)
s = defaultdict(set)
for line in data:
    d = [[int(jj) for jj in ii.split(",")] for ii in line.split(" -> ")]
    x1, y1 = d[0]
    for x2, y2 in d[1:]:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if y not in s[x1]:
                    bisect.insort(g[x1], y)
                s[x1].add(y)
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if y1 not in s[x]:
                    bisect.insort(g[x], y1)
                s[x].add(y1)
        x1, y1 = x2, y2

def dfs(x, y):
    idx = bisect.bisect_left(g[x], y)
    if idx >= len(g[x]):
        return False
    y = g[x][idx] - 1
    if y + 1 not in s[x - 1]:
        return dfs(x - 1, y + 1)
    if y + 1 not in s[x + 1]:
        return dfs(x + 1, y + 1)
    return x, y

num = 0
while True:
    n_pos = dfs(500, 0)
    if n_pos is False:
        break
    num += 1
    bisect.insort(g[n_pos[0]], n_pos[1])
    s[n_pos[0]].add(n_pos[1])
    print(num, n_pos)


# Part 2

from collections import defaultdict
import bisect

with open("day14.txt") as f:
    data = [ii.strip() for ii in f.readlines()]


g = defaultdict(list)
s = defaultdict(set)
y_max = 0
for line in data:
    d = [[int(jj) for jj in ii.split(",")] for ii in line.split(" -> ")]
    x1, y1 = d[0]
    for x2, y2 in d[1:]:
        y_max = max(y_max, y1, y2)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if y not in s[x1]:
                    bisect.insort(g[x1], y)
                s[x1].add(y)
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if y1 not in s[x]:
                    bisect.insort(g[x], y1)
                s[x].add(y1)
        x1, y1 = x2, y2

for x in range(min(g) - 300, max(g) + 300):
    bisect.insort(g[x], y_max + 2)
    s[x].add(y_max + 2)

def dfs(x, y):
    idx = bisect.bisect_left(g[x], y)
    if idx >= len(g[x]):
        return False
    y = g[x][idx] - 1
    if y + 1 not in s[x - 1]:
        return dfs(x - 1, y + 1)
    if y + 1 not in s[x + 1]:
        return dfs(x + 1, y + 1)
    return x, y

num = 0
while True:
    n_pos = dfs(500, 0)
    if n_pos == (500, 0):
        break
    num += 1
    bisect.insort(g[n_pos[0]], n_pos[1])
    s[n_pos[0]].add(n_pos[1])
    print(num, n_pos)

    

              


    

              
