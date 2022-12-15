import re
with open("day15.txt") as f:
    data = [ii.strip() for ii in f.readlines()]

res = set()
b = set()
# g = defaultdict(list)
target = 2000000

def get_range(x1, y1, x2, y2):
    if abs(target - y1) > abs(y1 - y2) + abs(x1 - x2):
        return 0
    return abs(y1 - y2) + abs(x1 - x2) - abs(target - y1)

for line in data:
    pa = re.findall(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line)
    x1, y1, x2, y2 = [int(ii) for ii in pa[0]]
    length = get_range(x1, y1, x2, y2)
    print(x1, y1, x2, y2, length)
    if y2 == target:
        b.add(x2)
    for ii in range(x1 - length, x1 + length + 1):
        res.add(ii)
for ii in b:
    res.remove(ii)

## Part 2

import re
with open("day15.txt") as f:
    data = [ii.strip() for ii in f.readlines()]

res = set()
g = []

N = 4000000
# d = [[-1] * N for ii in range(N)]

for line in data:
    pa = re.findall(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line)
    x1, y1, x2, y2 = [int(ii) for ii in pa[0]]
    length = abs(y1 - y2) + abs(x1 - x2)
    g.append((x1, y1, length))


for target in range(N):
    x = [[x1 - (length - abs(target - y1)), x1 + (length - abs(target - y1))] for x1, y1, length in g if abs(target - y1) <= length]
    x = sorted(x)
    res = [x[0]]
    for ii in x[1:]:
        if res[-1][1] >= ii[0]:
            res[-1][1] = max(res[-1][1], ii[1])
        else:
            m, n = target, res[-1][1] + 1
            print(m, n, (n * 4000000) + m)
            break


