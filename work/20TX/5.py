# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-23 21:08:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-23 21:57:34


import sys


def dijkstra(b: int, n: int, g: dict):
    # print("   ", b, n, g)
    dist = [float("inf")] * n
    dist[b] = 0
    flag = [False] * n
    for k, v in g[b + 1].items():
        dist[k - 1] = v
    for ii in range(n):
        t, min_val = None, float("inf")
        for jj in range(n):
            if not flag[jj] and dist[jj] < min_val:
                t, min_val = jj, dist[jj]

        if t is None:
            break
        flag[t] = True
        # print(t, dist)
        for k, v in g[t + 1].items():
            k -= 1
            if not flag[k] and dist[t] + v < dist[k]:
                dist[k] = dist[t] + v
    return dist[n - 1]


def get_dijkstra():
    n, m, k = [int(ii) for ii in sys.stdin.readline().strip().split()]
    g = {ii + 1: {} for ii in range(n)}
    for _ in range(m):
        a, b, c = [int(ii) for ii in sys.stdin.readline().strip().split()]
        if b in g[a]:
            g[a][b] = min(g[a][b], c)
        else:
            g[a][b] = c
        if a in g[b]:
            g[b][a] = min(g[b][a], c)
        else:
            g[b][a] = c
    for _ in range(k):
        a, b = [int(ii) for ii in sys.stdin.readline().strip().split()]
        g[a][b] = 0
    res = dijkstra(0, n, g)
    print(-1 if res == float("inf") else res)


get_dijkstra()

