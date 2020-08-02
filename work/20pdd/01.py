# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-02 18:57:03
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-02 19:11:51

import sys


K, N = [int(ii) for ii in sys.stdin.readline().strip().split()]
D = [int(ii) for ii in sys.stdin.readline().strip().split()]


def get_final_pos():
    res, final = K, 0
    for ii in D:
        # print(ii, res, final)
        res -= ii % 2 * K
        if res == 0:
            return "paradox"
        if res < 0:
            res *= -1
            final += 1
    return "{} {}".format(res, final)


print(get_final_pos())

