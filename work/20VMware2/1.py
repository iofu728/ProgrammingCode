# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-26 08:36:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-26 09:29:08

import sys
import bisect

N, M, T = [int(ii) for ii in sys.stdin.readline().strip().split()]
A = [int(ii) % T for ii in sys.stdin.readline().strip().split()]
B = [int(ii) % T for ii in sys.stdin.readline().strip().split()]


def get_min_mod():
    a, b = sorted(A), sorted(B)
    res = T
    for ii in a:
        res = min(res, (ii + b[0]) % T)
        idx = bisect.bisect_left(b, T - ii)
        for jj in range(idx, idx + 2):
            if jj < M:
                res = min(res, (ii + b[jj]) % T)
    print(res)


get_min_mod()
