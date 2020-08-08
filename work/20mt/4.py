# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-08 17:50:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-08 17:54:08

import sys

N = int(sys.stdin.readline())
D = [int(ii) for ii in sys.stdin.readline().strip().split()]


def get_bonus():
    tt = [[ii, D[ii]] for ii in range(1, len(D)) if D[ii] == D[ii - 1]]
    while len(tt):
        tt = sorted(tt, key=lambda i: (-i[1], i[0]))


print(get_dis())

