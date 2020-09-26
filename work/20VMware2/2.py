# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-26 09:29:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-26 10:26:46

import sys
from functools import lru_cache


@lru_cache(None)
def get_C(a: int, b: int):
    if b > a or b < 0:
        return 1
    if b > a // 2:
        return get_C(a, a - b)
    if b == 0:
        return 1
    if b == 1:
        return a
    if a == b:
        return 1
    if a == b + 1:
        return a
    return int(get_C(a - 1, b) * (a) / (a - b))


def get_retain():
    MODS = 998244353
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    A = [0] * N
    for _ in range(M):
        l, r, v = [int(ii) for ii in sys.stdin.readline().strip().split()]
        for ii in range(l - 1, r):
            # print("#", ii, ii - l + 1 + v, v, get_C(ii - l + 1 + v, v) % MODS)
            A[ii] = (get_C(ii - l + 1 + v, v) + A[ii]) % MODS
    print(" ".join([str(ii) for ii in A]))


get_retain()
