# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-07-04 13:22:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-07-04 13:22:14

"""
5803. 最长公共子路径 显示英文描述 
通过的用户数83
尝试过的用户数487
用户总通过次数111
用户总提交次数1488
题目难度Hard
一个国家由 n 个编号为 0 到 n - 1 的城市组成。在这个国家里，每两个 城市之间都有一条道路连接。

总共有 m 个编号为 0 到 m - 1 的朋友想在这个国家旅游。他们每一个人的路径都会包含一些城市。每条路径都由一个整数数组表示，每个整数数组表示一个朋友按顺序访问过的城市序列。同一个城市在一条路径中可能 重复 出现，但同一个城市在一条路径中不会连续出现。

给你一个整数 n 和二维数组 paths ，其中 paths[i] 是一个整数数组，表示第 i 个朋友走过的路径，请你返回 每一个 朋友都走过的 最长公共子路径 的长度，如果不存在公共子路径，请你返回 0 。

一个 子路径 指的是一条路径中连续的城市序列。

 

示例 1：

输入：n = 5, paths = [[0,1,2,3,4],
                     [2,3,4],
                     [4,0,1,2,3]]
输出：2
解释：最长公共子路径为 [2,3] 。
示例 2：

输入：n = 3, paths = [[0],[1],[2]]
输出：0
解释：三条路径没有公共子路径。
示例 3：

输入：n = 5, paths = [[0,1,2,3,4],
                     [4,3,2,1,0]]
输出：1
解释：最长公共子路径为 [0]，[1]，[2]，[3] 和 [4] 。它们长度都为 1 。
 

提示：

1 <= n <= 105
m == paths.length
2 <= m <= 105
sum(paths[i].length) <= 105
0 <= paths[i][j] < n
paths[i] 中同一个城市不会连续重复出现。
"""


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        if len(paths) == 1:
            return len(paths[0])
        S = 10 ** 9 + 7
        lth = [len(p) for p in paths]
        M = max(lth)
        b = [[11], [13]]
        for k in range(len(b)):
            for i in range(M):
                b[k].append(b[k][-1] * b[k][0] % S)
        a = []
        for p in paths:
            now = []
            for k in range(len(b)):
                tmp = [0]
                for i in range(len(p)):
                    tmp.append((tmp[-1] + p[i] * b[k][i]) % S)
                now.append(tmp)
            a.append(now)
        l, r = 1, min(lth)
        while l <= r:
            o = (l + r) >> 1
            c = collections.Counter()
            for av in a:
                now = set()
                for i in range(len(av[0]) - o):
                    tmp = []
                    for k in range(len(b)):
                        x = (av[k][i + o] - av[k][i]) * b[k][M - i] % S
                        tmp.append(x)
                    now.add(tuple(tmp))
                for x in now:
                    c[x] += 1
            flag = False
            for x in c:
                if c[x] == len(paths):
                    flag = True
                    break
            if flag:
                l = o + 1
            else:
                r = o - 1
        return r
