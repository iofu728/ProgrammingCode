with open("day18.txt") as f:
    data = [tuple(int(jj) for jj in ii.strip().split(",")) for ii in f.readlines()]

g = set(data)

def adj(p):
    for axis in range(3):
        for d in (-1, 1):
            q = list(p)
            q[axis] += d
            yield tuple(q)

print(sum(1 for p in g for q in adj(p) if q not in g))

P_min = tuple(min(p[axis] for p in g) - 1 for axis in range(3))
P_max = tuple(max(p[axis] for p in g) + 1 for axis in range(3))
stack = [P_min]
visited = set()
sa = 0
while stack:
    p = stack.pop()
    if p in visited:
        continue
    visited.add(p)
    for q in adj(p):
        if q in g:
            sa += 1
        if q not in g and q not in visited and all(l <= v <= u for l, v, u in zip(P_min, q, P_max)):
            stack.append(q)
print(sa)
