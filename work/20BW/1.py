# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-11 11:02:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-11 11:14:32

import sys
from collections import defaultdict


def get_rank():
    n, m = [int(ii) for ii in sys.stdin.readline().strip().split()]
    t = defaultdict(int)
    for _ in range(n):
        ii, jj = sys.stdin.readline().strip().split()
        jj = int(jj)
        t[ii] += jj
    tt = sorted(t.keys(), key=lambda i: (-t[i], i))
    if len(tt) > m:
        idx, pre = m - 1, t[tt[m - 1]]
        while idx + 1 < len(tt) and t[tt[idx + 1]] == pre:
            idx += 1
    else:
        idx = m - 1
    print(" ".join(tt[: idx + 1]))


get_rank()
