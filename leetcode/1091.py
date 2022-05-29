"""
1091. 二进制矩阵中的最短路径
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：

路径途经的所有单元格都的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。

 

示例 1：


输入：grid = [[0,1],[1,0]]
输出：2
示例 2：


输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4
示例 3：

输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1
 

提示：

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] 为 0 或 1
通过次数43,958提交次数114,434
"""
class Solution:
    DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(x, y):
            if (x, y) == (N - 1, M - 1):
                return 0
            res = float('inf')
            for dx, dy in self.DIRS:
                xx, yy = dx + x, dy + y
                if 0 <= xx < N and 0 <= yy < M and grid[xx][yy] == 0 and (xx, yy) not in done:
                    done.add((xx, yy))
                    res = min(res, dp(xx, yy) + 1)
            return res
            
        N, M = len(grid), len(grid[0])
        done = set([(0, 0)])
        q = []
        if grid[0][0] == 0:
            q.append((1, 0, 0))
        while q:
            h, x, y = heapq.heappop(q)
            if (x, y) == (N - 1, M - 1):
                return h
            for dx, dy in self.DIRS:
                xx, yy = dx + x, dy + y
                if 0 <= xx < N and 0 <= yy < M and grid[xx][yy] == 0 and (xx, yy) not in done:
                    done.add((xx, yy))
                    heapq.heappush(q, (h + 1, xx, yy))
        return -1
        