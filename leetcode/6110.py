# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-03 11:29:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-03 11:29:25

"""
6110. 网格图中递增路径的数目 显示英文描述 
通过的用户数32
尝试过的用户数40
用户总通过次数32
用户总提交次数47
题目难度Hard
给你一个 m x n 的整数网格图 grid ，你可以从一个格子移动到 4 个方向相邻的任意一个格子。

请你返回在网格图中从 任意 格子出发，达到 任意 格子，且路径中的数字是 严格递增 的路径数目。由于答案可能会很大，请将结果对 109 + 7 取余 后返回。

如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。

 

示例 1：



输入：grid = [[1,1],[3,4]]
输出：8
解释：严格递增路径包括：
- 长度为 1 的路径：[1]，[1]，[3]，[4] 。
- 长度为 2 的路径：[1 -> 3]，[1 -> 4]，[3 -> 4] 。
- 长度为 3 的路径：[1 -> 3 -> 4] 。
路径数目为 4 + 3 + 1 = 8 。
示例 2：

输入：grid = [[1],[2]]
输出：3
解释：严格递增路径包括：
- 长度为 1 的路径：[1]，[2] 。
- 长度为 2 的路径：[1 -> 2] 。
路径数目为 2 + 1 = 3 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 105
"""
class Solution:
    DIRS = [(0, 1), (1, 0)]
    MODS = 10 ** 9 + 7
    def countPaths(self, grid: List[List[int]]) -> int:
        def encode(x, y):
            return x * M + y
        def decode(x):
            return [x // M, x % M]
        @lru_cache(None)
        def dfs(x, y):
            res = 0
            for s in g[encode(x, y)]:
                xx, yy = decode(s)
                res += (1 + dfs(xx, yy))
            return res % self.MODS
        N, M = len(grid), len(grid[0])
        res = N * M
        g = defaultdict(list)
        for ii in range(N):
            for jj in range(M):
                for dx, dy in self.DIRS:
                    xx, yy = dx + ii, dy + jj
                    if 0 <= xx < N and 0 <= yy < M and grid[ii][jj] != grid[xx][yy]:
                        if grid[ii][jj] > grid[xx][yy]:
                            g[encode(ii, jj)].append(encode(xx, yy))
                        else:
                            g[encode(xx, yy)].append(encode(ii, jj))
        for ii in range(N):
            for jj in range(M):
                # print(dfs(ii, jj))
                res = (dfs(ii, jj) + res) % self.MODS
        return res
        
                
        