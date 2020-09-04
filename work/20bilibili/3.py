# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-04 20:08:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-04 20:17:54

import sys

T = int(sys.stdin.readline().strip())
A = [int(ii) for ii in sys.stdin.readline().strip().split()]


def get_nums(arr: str):
    pre = arr
    res = 0
    while len(pre):
        N = len(pre)
        b = [0] + [ii for ii in range(1, N) if pre[ii] > pre[ii - 1]]
        # print(pre, b, N)
        if len(b) == len(pre):
            break
        res += 1
        pre = [pre[ii] for ii in b]

    return res


print(get_nums(A))

