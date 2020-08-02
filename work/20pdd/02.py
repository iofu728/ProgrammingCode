# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-02 18:57:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-02 19:41:46

import sys


M = int(sys.stdin.readline().strip())
D = []
for ii in range(M):
    D.append([int(ii) for ii in sys.stdin.readline().strip().split()])


# def is_same(a, b):
#     a =


def up(a):
    a, b, c, d, e, f = a
    return [c, d, b, a, e, f]


def left(a):
    a, b, c, d, e, f = a
    return [a, b, f, e, c, d]


def dd(a):
    a, b, c, d, e, f = a
    return [e, f, c, d, b, a]


def decoder_once(a):
    find_1 = a.index(1)
    if find_1 == 1:
        a = up(up(a))
    elif find_1 == 2:
        a = up(a)
    elif find_1 == 3:
        a = up(up(up(a)))
    elif find_1 == 4:
        a = dd(a)
    elif find_1 == 5:
        a = dd(dd(dd(a)))
    find_2 = a.index(2)
    if find_2 == 1:
        find_2 = a.index(3)
    if find_2 == 3:
        a = left(left(a))
    elif find_2 == 4:
        a = left(left(left(a)))
    elif find_2 == 5:
        a = left(a)
    return a


def get_calculation():
    res = {}
    for jj in D:
        ii = decoder_once(jj)
        # print(jj, ii)
        if tuple(ii) not in res:
            res[tuple(ii)] = 0
        res[tuple(ii)] += 1
    print(len(res))
    print(" ".join([str(ii) for ii in sorted(res.values(), reverse=True)]))


get_calculation()

