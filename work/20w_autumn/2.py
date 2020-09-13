# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-13 18:55:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-13 21:04:21


import sys
import math


def get_time():
    def dijkstra(b: int, n: int, g: dict, T):
        # print("   ", b, n, g)
        dist = T
        dist[b] = 0
        flag = [False] * n
        for k in range(b + 1, n):
            dist[k] = min(dist[k], g[b][k])
        for ii in range(n):
            t, min_val = None, float("inf")
            for jj in range(n):
                if not flag[jj] and dist[jj] < min_val:
                    t, min_val = jj, dist[jj]

            if t is None:
                break
            flag[t] = True
            # print(t, dist)
            for k in range(t + 1, n):
                if not flag[k] and dist[t] + g[t][k] < dist[k]:
                    dist[k] = dist[t] + g[t][k]
        return dist[n - 1]

    N, X = [int(ii) for ii in sys.stdin.readline().strip().split()]
    t = int(sys.stdin.readline().strip())
    T = [int(ii) / t for ii in sys.stdin.readline().strip().split()]
    g = {ii: {} for ii in range(N - 1)}
    for ii in range(N - 1):
        tmp = [int(ii) for ii in sys.stdin.readline().strip().split()]
        for jj in range(N - 1 - ii):
            g[ii][ii + jj + 1] = tmp[jj] / t
    for ii in range(N - 1):
        tmp = [int(ii) for ii in sys.stdin.readline().strip().split()]
        for jj in range(N - 1 - ii):
            g[ii][ii + jj + 1] += tmp[jj]

    return dijkstra(X - 1, N, g, T)


print(get_time())
