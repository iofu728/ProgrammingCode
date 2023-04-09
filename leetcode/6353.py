# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-04-09 12:11:37
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-04-09 12:11:47

"""
6353. 网格图中最少访问的格子数 显示英文描述 
通过的用户数3
尝试过的用户数17
用户总通过次数3
用户总提交次数19
题目难度Hard
给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。

当你在格子 (i, j) 的时候，你可以移动到以下格子之一：

满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者
满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。
请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。

 

示例 1：



输入：grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
输出：4
解释：上图展示了到达右下角格子经过的 4 个格子。
示例 2：



输入：grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
输出：3
解释：上图展示了到达右下角格子经过的 3 个格子。
示例 3：



输入：grid = [[2,1,0],[1,0,0]]
输出：-1
解释：无法到达右下角格子。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= grid[i][j] < m * n
grid[m - 1][n - 1] == 0
"""
from sortedcontainers import SortedList

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[-1] * n for _ in range(m)]
        f[0][0] = 1
        rows = [SortedList(range(0, n)) for _ in range(m)]
        cols = [SortedList(range(0, m)) for _ in range(n)]
        q = [[0, 0]]
        index = 0
        while index < len(q):
            x, y = q[index]
            index += 1
            sl = rows[x]
            while True:
                pos = sl.bisect_left(y + 1)
                if pos == len(sl):
                    break
                ny = sl[pos]
                # print(ny)
                if ny > y + grid[x][y]:
                    break
                f[x][ny] = f[x][y] + 1
                q.append([x, ny])
                del sl[pos]
                cols[ny].remove(x)
            sl = cols[y]
            while True:
                pos = sl.bisect_left(x + 1)
                if pos == len(sl):
                    break
                nx = sl[pos]
                if nx > x + grid[x][y]:
                    break
                f[nx][y] = f[x][y] + 1
                q.append([nx, y])
                del sl[pos]
                rows[nx].remove(y)
        return f[-1][-1]