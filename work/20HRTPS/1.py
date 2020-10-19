# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-10 19:42:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-10 19:47:38

import sys

N = int(sys.stdin.readline())


def get_i():
    A = [int(ii) for ii in sys.stdin.readline().strip().split()]
    pre, res = A[0], 1
    for ii in A[1:]:
        if ii <= pre:
            res += 1
            pre = ii
    return res


print(get_i())
