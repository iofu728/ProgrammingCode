# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-08 20:11:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-08 21:07:31

"""
面试题13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

## 示例 1：
输入：m = 2, n = 3, k = 1
输出：3

## 示例 2：
输入：m = 3, n = 1, k = 0
输出：1

## 提示：
1 <= n,m <= 100
0 <= k <= 20
通过次数22,387提交次数46,542
"""


class Solution:
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def movingCount(self, m: int, n: int, k: int) -> int:
        flag = [[0 for _ in range(n)] for _ in range(m)]

        def is_ok(x: int, y: int) -> bool:
            return sum([int(ii) for ii in str(x) + str(y)]) <= k

        def dfs(x: int, y: int):
            for dx, dy in self.DIR:
                x, y = x + dx, y + dy
                if -1 < x < m and -1 < y < n and is_ok(x, y) and not flag[x][y]:
                    flag[x][y] = 1
                    dfs(x, y)

        dfs(0, 0)
        return len([1 for ii in flag for jj in ii if jj])
