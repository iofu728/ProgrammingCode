# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-21 19:25:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-21 20:08:09


def test(input1):
    N = len(input1)
    if N >> 1 << 1 != N:
        return -1
    return sum(
        [int(input1[ii] != "K") + int(input1[ii + 1] != "J") for ii in range(0, N, 2)]
    )
