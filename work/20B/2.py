# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-12 19:47:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-12 20:49:54

import heapq
import sys


def get_rank():
    def dfs(vis, num):

        for ii in range(1, n + 1):
            if vis[ii] == 0:
                if ii == t:
                    res.add(num + 1)
                    continue
                vis[ii] -= 1
                for kk in g[ii]:
                    vis[kk] -= 1
                dfs(vis, num + 1)
                vis[ii] += 1
                for kk in g[ii]:
                    vis[kk] += 1

    n, m, t = [int(ii) for ii in sys.stdin.readline().strip().split()]
    g, vis = {ii: set() for ii in range(n + 1)}, [0] * (n + 1)
    for _ in range(m):
        ii, jj = [int(ii) for ii in sys.stdin.readline().strip().split()]
        if jj not in g[ii]:
            g[ii].add(jj)
            vis[jj] += 1
    flag = [(jj, ii) for ii, jj in enumerate(vis)]
    heapq.heapify(flag)
    res = set()
    dfs(flag, 0)
    return res


print(" ".join([str(ii) for ii in sorted(get_rank())]))
