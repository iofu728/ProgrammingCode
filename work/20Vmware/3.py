# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-21 21:41:04
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-21 21:52:52

import sys
from collections import defaultdict

n, K = [int(ii) for ii in sys.stdin.readline().strip().split()]


def get_tref():
    g, gg = defaultdict(int), defaultdict(int)

    for ii in range(n):
        ii, jj = [int(ii) for ii in sys.stdin.readline().strip().split()]
        if ii > jj:
            ii, jj = jj, ii
        g[ii] += 1
        g[jj] += 1
        gg[(ii, jj)] += 1
    res = 0
    tt = sorted(g.items(), key=lambda x: -x[1])
    N = len(tt)
    for ii, (k, v) in enumerate(tt):
        if v >= K:
            res += n - ii
            continue
        for jj in range(ii + 1, N):
            if tt[jj][1] + v < K:
                break
            tmp_k, tmp_v = tt[jj]
            if tmp_v + v - (gg[(k, tmp_k)] if k < tmp_k else gg[(tmp_k, k)]) >= K:
                res += 1
    print(res)


get_tref()

