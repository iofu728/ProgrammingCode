# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-11 11:06:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-12 00:00:04

import sys


def get_times():
    n, m = [int(ii) for ii in sys.stdin.readline().strip().split()]
    if n * m >> 1 << 1 != n * m:
        return -1
    dp1 = [[0] * (m + 1) for _ in range(n + 1)]
    dp2 = [[0] * (m + 1) for _ in range(n + 1)]
    dp3 = [[0] * (m + 1) for _ in range(n + 1)]
    dp4 = [[0] * (m + 1) for _ in range(n + 1)]
    dp3[0] = [0] + [1] * (m)
    for ii in range(1, n + 1):
        dp3[ii][0] = 1
    for ii in range(1, n + 1):
        for jj in range(1, m + 1):
            print(
                (dp2[ii - 1][jj] + dp3[ii - 1][jj]), (dp3[ii][jj - 1] + dp1[ii][jj - 1])
            )
            dp1[ii][jj] = (
                (dp2[ii - 1][jj] + dp3[ii - 1][jj])
                * (dp3[ii][jj - 1] + dp1[ii][jj - 1])
                * int(ii < n)
            )
            dp2[ii][jj] = (dp3[ii][jj - 1] + dp1[ii][jj - 1]) * int(jj < m)
            dp3[ii][jj] = dp2[ii][jj - 1]
            dp4[ii][jj] = dp1[ii - 1][jj]
    print(dp1)
    print(dp2)
    print(dp3)
    return dp1[-1][-1] + dp2[-1][-1] + dp3[-1][-1]


print(get_times())
