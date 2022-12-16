import re
from functools import lru_cache
from collections import defaultdict

with open("day16.txt") as f:
    data = [ii.strip() for ii in f.readlines()]

g = defaultdict(set)
v = defaultdict(int)
for line in data:
    m = re.findall(r"Valve (.*) has flow rate=(\d*); tunnel lead to valve (.*)", line.replace("valves", "valve").replace("tunnels", "tunnel").replace("leads", "lead"))
    ii, jj, kk = m[0]
    for k in kk.split(","):
        k = k.strip()
        g[ii].add(k)
    v[ii] = int(jj)

g_ids = {jj: ii for ii, jj in enumerate(g.keys()) if v[jj] > 0}
@lru_cache(None)
def dfs(x, t, done):
    if t >= 26:
        return dfs2("AA", 0, done)
    res = 0
    target = (26 - t - 1) * v[x]
    a = ""
    idx = g_ids.get(x, 0)

    if target > 0 and (done | (1 << idx)) != done:
        tmp_done = (done | (1 << idx))
        for y in g[x]:
            if dfs(y, t + 2, tmp_done) + target > res:
                a = f"in{x}->{y}, {tmp_done}"
                res = dfs(y, t + 2, tmp_done) + target

    for y in g[x]:
        if dfs(y, t + 1, done) > res:
            a = f"->{y}"
            res = max(dfs(y, t + 1, done), res)

    print(x, t, a, res)
    return res

@lru_cache(None)
def dfs2(x, t, done):
    if t >= 26:
        return 0
    res = 0
    target = (26 - t - 1) * v[x]
    a = ""
    idx = g_ids.get(x, 0)

    if target > 0 and (done | (1 << idx)) != done:
        tmp_done = (done | (1 << idx))
        for y in g[x]:
            if dfs2(y, t + 2, tmp_done) + target > res:
                a = f"in{x}->{y}, {tmp_done}"
                res = dfs2(y, t + 2, tmp_done) + target

    for y in g[x]:
        if dfs2(y, t + 1, done) > res:
            a = f"->{y}"
            res = max(dfs2(y, t + 1, done), res)

    print(x, t, a, res)
    return res

dfs("AA", 0, 0)

