# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-23 20:38:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-23 20:49:00


import sys

MOD = 10 ** 9 + 7


def quick_mod(num: int):
    if num == 0:
        return 1
    if num == 1:
        return 2
    t = num >> 1

    tmp = quick_mod(t)
    if t << 1 == num:
        return (tmp % MOD) ** 2
    return 2 * ((tmp % MOD) ** 2)


def get_nums():
    T = int(sys.stdin.readline().strip())
    num = (T % MOD) * (quick_mod(T - 1)) % (MOD)
    print(num)


get_nums()

