# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-21 21:23:50
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-21 21:40:01

import sys

T = int(sys.stdin.readline())


def get_ok():
    N = int(sys.stdin.readline())
    A = [int(ii) for ii in sys.stdin.readline().strip().split()]
    B = [int(ii) for ii in sys.stdin.readline().strip().split()]
    flag = [False] * N
    Ag = {jj: ii for ii, jj in enumerate(A)}
    for b, jj in enumerate(B):
        e = Ag[jj]
        if e < b:
            b, e = e, b
        for ii in range(b, e + 1):
            if flag[ii]:
                continue
            if B[ii] != jj and b <= Ag[B[ii]] <= e:
                return "NO"
            flag[ii] = True
    return "YES"


for ii in range(T):
    print(get_ok())

