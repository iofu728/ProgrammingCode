with open("day4.txt") as f:
    data = [[[int(kk) for kk in jj.split("-")] for jj in ii.strip().split(",")] for ii in f.readlines()]

res = 0
for line in data:
    d = sorted(line, key=lambda x: (x[0], -x[1]))
    if d[0][0] <= d[1][1] <= d[0][1]:
        print(line)
        res += 1

res = 0
for line in data:
    d = sorted(line, key=lambda x: (x[0], -x[1]))
    if d[0][1] >= d[1][0]:
        print(line)
        res += 1

