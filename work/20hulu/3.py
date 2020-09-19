# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-16 20:54:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-16 20:54:19

"""
迷宫寻宝
时间限制： 3000MS
内存限制： 589824KB
题目描述：
一个N*M*L的3D迷宫，其中藏有若干个稀世宝石，迷宫中每一格可以是道路、陷阱或者宝石，进入陷阱游戏失败(宝石清零)。每颗宝石有不同的价值，拿到宝石并返回到迷宫的起点则可以获取对应的宝石。给定一个起点，每次可以选择往相邻上、下、东、西、南、北6个方向移动一格，判断可以获取的总的宝石价值最多为多少，以及拿回这些宝石（即返回到起点）所需要的最小步数。



输入描述
第一行为三个空格分开的正整数 N，M，L

接下来会依次展示L层迷宫，每层迷宫包含N行M列，每一行都是以空格分开的数字。其中-2表示陷阱，-1表示迷宫起点，0表示道路，其他正整数表示宝石价值V。

 

数据范围：

1<=N, M, L<=30, 1<=宝石总颗数<=10， 1<=单个宝石的价值V<=100000

输出描述

输出两个以空格分开的整数，分别表示最多可以获取的宝石价值以及拿回这些宝石所需要的最小步数。


样例输入
2 2 2
0  3
4 -2
0  0
1 -1
样例输出
8 6
"""
import sys

DIRS = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0)]
N, M, T = [int(ii) for ii in sys.stdin.readline().strip().split()]

def get_a():
    def dfs(x, y, z, value, step):
        nonlocal res, steps, g
        print(x, y, z, value, step)
        step += 1
        if g[x][y][z] != -1:
            value += g[x][y][z]
            g[x][y][z] = 0
        if x == pi and y == pj and z == pk:
            if value:
                if res < value:
                    res = value
                    steps = step
                elif res == value:
                    steps = min(step, steps)
        for dx, dy, dz in DIRS:
            xx, yy, zz = dx + x, dy + y, dz + z
            print(xx, yy, zz)
            if not (0 <= xx < N) or not (0 <= yy < M) or not (0 <= zz < T) or g[xx][yy][zz] in [-2]:
                continue
            dfs(xx, yy, zz, value, step)
                
    g = [[[0] * T for _ in range(M)] for _ in range(N)]
    pi, pj, pk = 0, 0, 0
    res, steps = 0, -1
    ## dp = [[[False] * T for _ in range(M)] for _ in range(N)]
    for kk in range(T):
        for ii in range(N):
            for jj, v in enumerate([int(ii) for ii in sys.stdin.readline().strip().split()]):
                g[ii][jj][kk] = v
                if v == -1:
                    pi, pj, pk = ii, jj, kk
    print(pi, pj, pk)
    dfs(pi, pj, pk, 0, -1)
    
    print("{} {}".format(res, steps))
    
get_a()
    
