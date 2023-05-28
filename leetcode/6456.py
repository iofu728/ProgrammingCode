# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-05-28 11:47:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-05-28 11:47:13

"""
6456. 矩阵中严格递增的单元格数 显示英文描述 
通过的用户数96
尝试过的用户数297
用户总通过次数102
用户总提交次数442
题目难度Hard
给你一个下标从 1 开始、大小为 m x n 的整数矩阵 mat，你可以选择任一单元格作为 起始单元格 。

从起始单元格出发，你可以移动到 同一行或同一列 中的任何其他单元格，但前提是目标单元格的值 严格大于 当前单元格的值。

你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。

请你找出从某个单元开始访问矩阵所能访问的 单元格的最大数量 。

返回一个表示可访问单元格最大数量的整数。

 

示例 1：



输入：mat = [[3,1],[3,4]]
输出：2
解释：上图展示了从第 1 行、第 2 列的单元格开始，可以访问 2 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 2 个单元格，因此答案是 2 。 
示例 2：



输入：mat = [[1,1],[1,1]]
输出：1
解释：由于目标单元格必须严格大于当前单元格，在本示例中只能访问 1 个单元格。 
示例 3：



输入：mat = [[3,1,6],[-9,5,7]]
输出：4
解释：上图展示了从第 2 行、第 1 列的单元格开始，可以访问 4 个单元格。可以证明，无论从哪个单元格开始，最多只能访问 4 个单元格，因此答案是 4 。  
 

提示：

m == mat.length 
n == mat[i].length 
1 <= m, n <= 105
1 <= m * n <= 105
-105 <= mat[i][j] <= 105
"""
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(x, y):
            res = 1
            # print(x, y)
            # print(xxx[x], (mat[x][y], 10 ** 6))
            x_idx = bisect.bisect(xxx[x], (mat[x][y], 10 ** 6))
            pre = None
            for dx in range(x_idx, M):
                if pre is not None and pre != xxx[x][dx][0]:
                    break
                xx, yy = x, xxx[x][dx][1]
                res = max(res, dfs(xx, yy) + 1)
                pre = xxx[x][dx][0]
            y_idx = bisect.bisect(yyy[y], (mat[x][y], 10 ** 6))
            pre = None
            for dy in range(y_idx, N):
                if pre is not None and pre != yyy[y][dy][0]:
                    break
                xx, yy = yyy[y][dy][1], y
                res = max(res, dfs(xx, yy) + 1)
                pre = yyy[y][dy][0]
            # for dx, dy in self.DIRS:
            #     xx, yy = x + dx, y + dy
            #     if (0 <= xx < N) and (0 <= yy < M) and mat[xx][yy] > mat[x][y]:
            #         res = max(res, dfs(xx, yy) + 1)
            return res
        
        
        N, M = len(mat), len(mat[0])
        xxx, yyy = [sorted([(k, j) for j, k in enumerate(mat[ii])]) for ii in range(N)], [sorted([(mat[j][ii], j) for j in range(N)]) for ii in range(M)]
        ans = 1
        for ii in range(N):
            jj = xxx[ii][0][1]
            ans = max(ans, dfs(ii, jj))
        for jj in range(M):
            ii = yyy[jj][0][1]
            ans = max(ans, dfs(ii, jj))
        return ans
        
        