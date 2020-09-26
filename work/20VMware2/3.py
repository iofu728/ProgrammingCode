# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-26 09:53:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-26 09:57:27

import sys


def get_color_num():
    N, X = [int(ii) for ii in sys.stdin.readline().strip().split()]
    A = [int(ii) for ii in sys.stdin.readline().strip().split()]
    sum_a = sum(A)
    if sum_a != 0:
        sum_a = abs(sum_a)
        return sum_a // X + (0 if sum_a % X == 0 else 1)
    return 0


print(get_color_num())
