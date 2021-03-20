# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-01-27 21:30:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-01-27 22:13:55
import sys

def get_num():
    A = sys.stdin.readline()
    A = list(set([int(ii) for ii in A.split(" ")]))
    B = int(sys.stdin.readline())
    C = int(sys.stdin.readline())
    if B > C or B not in A:
        return 0
    res = 1
    C -= B
    idx = A.index(B)
    A = A[:idx] + A[idx + 1:]
    N = len(A)

    dp = [[0 for i in range(C + 1)] for j in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1,C + 1):
            dp[i][j] = dp[i-1][j]
            if j >= A[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-A[i-1]]+1)

    print(dp)
    print(res + dp[-1][-1])

get_num()