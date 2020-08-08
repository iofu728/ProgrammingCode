# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-08 16:18:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-08 17:46:39

import sys

N = int(sys.stdin.readline())
D = [[int(ii) for ii in sys.stdin.readline().strip().split()] for _ in range(N - 1)]


def get_dis():
    MAP, MAP1, MAP2 = {}, {ii: [] for ii in range(1, N + 1)}, {}
    flags = [True] * N
    flags[0] = False
    for ii, jj, kk in D:
        MAP1[ii].append((jj, kk))
        MAP1[jj].append((ii, kk))
        if ii > jj:
            jj, ii = ii, jj
        if ii == 1:
            MAP2[jj] = kk
            MAP[jj] = kk

    def dfs(now):
        if len(MAP1[now]) == 1:
            return 0, 0
        tmp = []
        # print(now, MAP1[now])
        for ii, mm in MAP1[now]:
            if flags[ii - 1] != True:
                continue
            flags[ii - 1] = False
            aa, bb = dfs(ii)
            tmp.append((aa + mm, bb + mm))
        tmp = sorted(tmp, key=lambda i: i[0] + i[1])
        # print(tmp)
        return sum([sum(ii) for ii in tmp[:-1]]) + tmp[-1][0], tmp[-1][1]

    res = []

    def dfs1(now):
        if len(MAP1[now]) == 1:
            return 0
        tmp = []
        for ii, mm in MAP1[now]:
            if flags[ii - 1] != True:
                continue
            flags[ii - 1] = False
            cc = dfs1(ii)
            res.append((cc + 1) * mm)
            tmp.append(cc + 1)
        # print(tmp)
        return sum(tmp)

    aa, bb = dfs(1)

    flags = [True] * N
    flags[0] = False
    dfs1(1)
    # print(res)
    return "{} {}".format(sum(res), aa)


print(get_dis())

