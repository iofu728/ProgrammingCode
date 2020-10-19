# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-18 10:51:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-18 11:05:32

import sys



def get_set():
    def dfs(save, pre):
        nonlocal res
        if not save:
            res = max(pre, res)
            return
        for ii in range(len(save)):
            dfs(save[:ii] + save[ii + 1:], pre + A[N - len(save)][save[ii]])

    N = int(sys.stdin.readline())
    A = []
    for _ in range(N):
        A.append([int(ii) for ii in sys.stdin.readline().strip().split()])
    res = 0
    dfs(list(range(N)), 0)
    return res

print(get_set())
    