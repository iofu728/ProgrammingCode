# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-10 13:30:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-10 13:31:01

"""
100030. 将石头分散到网格图的最少移动次数 显示英文描述 
通过的用户数0
尝试过的用户数2
用户总通过次数0
用户总提交次数5
题目难度Medium
给你一个大小为 3 * 3 ，下标从 0 开始的二维整数矩阵 grid ，分别表示每一个格子里石头的数目。网格图中总共恰好有 9 个石头，一个格子里可能会有 多个 石头。

每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。

请你返回每个格子恰好有一个石头的 最少移动次数 。

 

示例 1：



输入：grid = [[1,1,0],[1,1,1],[1,2,1]]
输出：3
解释：让每个格子都有一个石头的一个操作序列为：
1 - 将一个石头从格子 (2,1) 移动到 (2,2) 。
2 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
3 - 将一个石头从格子 (1,2) 移动到 (0,2) 。
总共需要 3 次操作让每个格子都有一个石头。
让每个格子都有一个石头的最少操作次数为 3 。
示例 2：



输入：grid = [[1,3,0],[1,0,0],[1,0,3]]
输出：4
解释：让每个格子都有一个石头的一个操作序列为：
1 - 将一个石头从格子 (0,1) 移动到 (0,2) 。
2 - 将一个石头从格子 (0,1) 移动到 (1,1) 。
3 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
4 - 将一个石头从格子 (2,2) 移动到 (2,1) 。
总共需要 4 次操作让每个格子都有一个石头。
让每个格子都有一个石头的最少操作次数为 4 。
 

提示：

grid.length == grid[i].length == 3
0 <= grid[i][j] <= 9
grid 中元素之和为 9 。
"""
from scipy.optimize import linear_sum_assignment
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        a, b = [], set()
        q = []
        for ii in range(3):
            for jj in range(3):
                if grid[ii][jj] == 0:
                    b.add((ii, jj))
                elif grid[ii][jj] > 1:
                    a.append((ii, jj, grid[ii][jj] - 1))
        
        res = 10 ** 9 + 7
        def dfs(idx, y):
            if idx >= len(a):
                return 0
            ans = 10 ** 9 + 7
            ii, jj, kk = a[idx]
            for xs in combinations(list(y), kk):
                tmp = 0
                for i, j in xs:
                    tmp += abs(ii - i) + abs(jj - j)
                    y.remove((i, j))
                ans = min(ans, tmp + dfs(idx + 1, y))
                for i, j in xs:
                    y.add((i, j))
            return ans
        return dfs(0, b)
                
                
            
            
        