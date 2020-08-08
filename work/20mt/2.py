# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-08 16:07:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-08 16:17:31

import sys

N = int(sys.stdin.readline())
D = [[int(ii) for ii in sys.stdin.readline().strip().split()] for _ in range(N)]


def get_actual_money(a):
    a, b = a
    if b >= a:
        return 0
    return a - b


def get_max():
    A, B = 0, 0
    for ii, jj in D:
        if ii <= jj:
            A += jj
        else:
            A += ii
            B += ii - jj
    return "{} {}".format(A, B)


print(get_max())
