# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-24 11:47:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-24 11:47:44
"""
6125. 相等行列对 显示英文描述 
通过的用户数5
尝试过的用户数50
用户总通过次数5
用户总提交次数50
题目难度Medium
给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。

如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

 

示例 1：



输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
输出：1
解释：存在一对相等行列对：
- (第 2 行，第 1 列)：[2,7,7]
示例 2：



输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
输出：3
解释：存在三对相等行列对：
- (第 0 行，第 0 列)：[3,1,2,2]
- (第 2 行, 第 2 列)：[2,4,2,2]
- (第 3 行, 第 2 列)：[2,4,2,2]
 

提示：

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def is_same(x, y):
            idx = 0
            while idx < N:
                if grid[x][idx] != grid[idx][y]:
                    return False
                idx += 1
            return True

        N = len(grid)
        res = 0
        for ii in range(N):
            for jj in range(N):
                if is_same(ii, jj):
                    res += 1
        return res