# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-10 19:29:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-10 20:33:10

import sys

T = int(sys.stdin.readline().strip())


def get_time():
    def dfs(now, pre):
        nonlocal have, res
        # print(now, pre)
        if now not in q:
            n = len(pre)
            for ii in range(n):
                for jj in range(ii + 1, n):
                    have.add((pre[ii], pre[jj]))
            return
        for ii in q[now]:
            if (now, ii) not in have:
                dfs(ii, pre + [ii])
                res += 1

    N = int(sys.stdin.readline().strip())
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    s = {}
    for ii, jj in zip(a, b):
        if ii == jj:
            
        if ii not in s:
            s[ii] = set()
        if ii > jj:
            return -1
        if ii < jj:
            s[ii].add(jj)
    q = {ii: sorted(list(jj)) for ii, jj in s.items()}
    # print(q)
    have = set()
    res = 0
    for ii in sorted(q):
        dfs(ii, [ii])

    return res


for ii in range(T):
    print(get_time())

