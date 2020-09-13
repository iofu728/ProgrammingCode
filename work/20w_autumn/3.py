# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-13 18:55:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-13 21:29:26

import sys
import math


def get_origin(x, y):
    xx = (y + 1) * 0.5
    yy = (SQRT_3 / 2) * x + ((SQRT_3 / 3) if (x + y) >> 1 << 1 != (x + y) else (SQRT_3 / 6))
    return [xx, yy]


def is_close(A, B):
    if A == B:
        return True
    if sum(A) >> 1 << 1 == sum(A):
        return B in [[dx + A[0], dy + A[1]] for dx, dy in DIRS_ODD]
    return B in [[dx + A[0], dy + A[1]] for dx, dy in DIRS_SIN]


def ab_dis(A, B):
    a, b = get_origin(*A), get_origin(*B)
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


SQRT_3 = math.sqrt(3)
DIRS_ODD, DIRS_SIN = [(0, ii) for ii in range(-2, 3)], [(0, ii) for ii in range(-2, 3)]
for ii in range(-1, 2):
    DIRS_ODD.append((1, ii))
    DIRS_SIN.append((-1, ii))
for ii in range(-2, 3):
    DIRS_ODD.append((-1, ii))
    DIRS_SIN.append((1, ii))


def get_cos(A, B, x):
    if A == x:
        return -1
    a, b = get_origin(*A), get_origin(*B)
    AB = (B[0] - A[0], B[1] - A[1])
    Ax = (x[0] - A[0], x[1] - A[1])
    return (AB[0] * Ax[0] + AB[1] * Ax[1]) / (math.sqrt(AB[0]**2 + AB[1]**2) * math.sqrt(Ax[0]**2 + Ax[1]**2))


def get_dist():
    Ax, Ay, Bx, By = [int(ii) for ii in sys.stdin.readline().strip().split()]
    if Ax > Bx:
        Ax, Ay, Bx, By = Bx, By, Ax, Ay
    A, B = [Ax, Ay], [Bx, By]
    P = A
    res = 0
    t = 0
    while not is_close(P, B) and P != B and t < 10:
        if sum(P) >> 1 << 1 == sum(P):
            d = DIRS_ODD
        else:
            d = DIRS_SIN
        close = min(
            [[P[0] + dx, P[1] + dy] for dx, dy in d],
            key=lambda x: 1 - get_cos(A, B, x)
        )
        res += ab_dis(P, close)
        P = close
        # print(res, P, B)
        t += 1

    res += ab_dis(P, B)
    return res


print(get_dist())

