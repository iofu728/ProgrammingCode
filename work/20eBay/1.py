# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-16 19:29:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-16 19:41:30

import sys
from collections import defaultdict


def get_res():
    n, m = [int(ii) for ii in sys.stdin.readline().strip().split()]
    A = [0] * n
    res = defaultdict(int)
    for _ in range(m):
        a, b, c = [int(ii) for ii in sys.stdin.readline().strip().split()]
        res[a - 1] += c
        res[b] -= c
    idx, pre = 0, 0
    for ii in sorted(res.keys()):
        if pre != 0:
            for jj in range(idx, ii):
                A[jj] = pre
        idx = ii
        pre += res[ii]
    if pre != 0:
        for ii in range(idx, n):
            A[ii] = pre
    print(" ".join([str(ii) for ii in A]))


get_res()

