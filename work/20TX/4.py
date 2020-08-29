# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-23 20:49:28
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-23 21:07:43


import sys


def get_c(num: int):
    if num == 1:
        return 0
    return num * (num - 1) // 2


def get_graph():
    n, m = [int(ii) for ii in sys.stdin.readline().strip().split()]
    g = {ii + 1: set() for ii in range(n)}
    for _ in range(m):
        a, b = [int(ii) for ii in sys.stdin.readline().strip().split()]
        g[a].add(str(b))
        g[b].add(str(a))
    set_map = {}
    for ii in range(1, n + 1):
        tmp = ",".join(g[ii])
        if tmp not in set_map:
            set_map[tmp] = 1
        else:
            set_map[tmp] += 1
    res = sum([get_c(ii) for ii in set_map.values()])
    print(res)


get_graph()

