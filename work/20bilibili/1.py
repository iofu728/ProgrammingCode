# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-04 19:34:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-04 19:44:48

import sys

S = sys.stdin.readline().strip()


def get_same(s: str):
    N = len(s)
    if N == 0:
        return ""
    dp = [[0] * N for _ in range(N)]
    for ii in range(N):
        dp[ii][ii] = 1
    max_v, res = 1, s[0]
    for ii in range(N - 1, -1, -1):
        for kk in range(1, N - ii):
            jj = kk + ii
            if s[ii] == s[jj]:
                dp[ii][jj] = dp[ii + 1][jj - 1] + 2
                if dp[ii][jj] > max_v:
                    max_v = dp[ii][jj]
                    res = s[ii : jj + 1]

    return res


print(get_same(S))

