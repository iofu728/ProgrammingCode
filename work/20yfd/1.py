# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-24 19:18:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-24 19:28:26

import sys

T = int(sys.stdin.readline().strip())


def have_loop(case: int):
    def dfs(ii: int):
        nonlocal valid
        flag[ii] = 1
        for v in g[ii]:
            if flag[v] == 0:
                dfs(v)
                if not valid:
                    return
            elif flag[v] == 1:
                valid = False
                return
        flag[ii] = 2

    N = int(sys.stdin.readline())
    g = {}
    for ii in range(N):
        g[ii] = [
            jj
            for jj, i in enumerate(sys.stdin.readline().strip().split())
            if int(i) == 1
        ]
    valid = True
    flag = [0] * N
    for ii in range(N):
        if valid and flag[ii] == 0:
            dfs(ii)
        if not valid:
            return 1
    return int(valid == False)


for ii in range(T):
    print(have_loop(ii))
