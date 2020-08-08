# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-06 19:39:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-06 20:16:01

import sys
import math

N, M = [int(ii) for ii in sys.stdin.readline().strip().split()]


def is_prime(a: int) -> bool:
    if a == 1:
        return True
    for ii in range(int(math.sqrt(a)), 1, -1):
        if a % ii == 0:
            return False
    return True


def get_len(a: int):
    return len(str(a))


def get_comeback():
    res = []
    NL, ML = get_len(N), get_len(M)
    for ii in [2, 3, 5, 7, 11]:
        if ii <= M:
            res.append(ii)
        elif ii > M:
            break
    for ii in range(1, 10, 2):
        for jj in range(10):
            tmp = ii * 100 + jj * 10 + ii
            if tmp <= M:
                res.append(tmp)
            elif tmp > M:
                break

    for ii in range(1, 10, 2):
        for jj in range(10):
            for kk in range(10):
                tmp = ii * 10000 + jj * 1000 + kk * 100 + jj * 10 + ii
                if tmp <= M:
                    res.append(tmp)
                elif tmp > M:
                    break
    # print(res)
    return res


def get_comeback_one():
    can = get_comeback()
    res = 0
    ans = []
    have = set()
    for ii in can:
        ii = str(ii)
        for idx in range(len(ii) + 1):
            for jj in range(10):
                if idx == 0 and jj == 0:
                    continue
                tmp = int(ii[:idx] + str(jj) + ii[idx:])
                if N <= tmp <= M:
                    if tmp not in have:
                        res += 1
                        have.add(tmp)
                        ans.append(tmp)
    print(ans)
    return res


print(get_comeback_one())
