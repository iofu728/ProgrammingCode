# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-03-03 13:31:18
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-03-03 13:31:31

"""
100237. 元素和小于等于 k 的子矩阵的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个下标从 0 开始的整数矩阵 grid 和一个整数 k。

返回包含 grid 左上角元素、元素和小于或等于 k 的 子矩阵 的数目。

 

示例 1：


输入：grid = [[7,6,3],[6,6,1]], k = 18
输出：4
解释：如上图所示，只有 4 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 18 。
示例 2：


输入：grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
输出：6
解释：如上图所示，只有 6 个子矩阵满足：包含 grid 的左上角元素，并且元素和小于或等于 20 。
 

提示：

m == grid.length
n == grid[i].length
1 <= n, m <= 1000
0 <= grid[i][j] <= 1000
1 <= k <= 109
"""
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        N, M = len(grid), len(grid[0])
        s = []
        res = 0
        for ii in range(N):
            tmp = [0] * M
            x = 0
            for jj in range(M):
                x += grid[ii][jj]
                tmp[jj] = x + (s[-1][jj] if s else 0)
                if tmp[jj] <= k:
                    res += 1
            s.append(tmp)
        return res
                
        