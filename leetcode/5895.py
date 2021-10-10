# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-10 13:09:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-10 13:10:01

"""
5895. 获取单值网格的最小操作数 显示英文描述 
通过的用户数1442
尝试过的用户数2095
用户总通过次数1486
用户总提交次数5233
题目难度Medium
给你一个大小为 m x n 的二维整数网格 grid 和一个整数 x 。每一次操作，你可以对 grid 中的任一元素 加 x 或 减 x 。

单值网格 是全部元素都相等的网格。

返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 -1 。

 

示例 1：



输入：grid = [[2,4],[6,8]], x = 2
输出：4
解释：可以执行下述操作使所有元素都等于 4 ： 
- 2 加 x 一次。
- 6 减 x 一次。
- 8 减 x 两次。
共计 4 次操作。
示例 2：



输入：grid = [[1,5],[2,3]], x = 1
输出：5
解释：可以使所有元素都等于 3 。
示例 3：



输入：grid = [[1,2],[3,4]], x = 2
输出：-1
解释：无法使所有元素相等。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104
"""


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        M, N = len(grid), len(grid[0])
        min_v = min([min(ii) for ii in grid])
        gap = []
        for ii in grid:
            for jj in ii:
                if (jj - min_v) % x:
                    return -1
                gap.append((jj - min_v) // x)
        gap_c = Counter(gap)
        gap = sorted(gap_c.keys())
        # print(gap)
        sum_g, num_g = [0], [0]
        for ii in gap:
            sum_g.append(sum_g[-1] + ii * gap_c[ii])
            num_g.append(num_g[-1] + gap_c[ii])
        res = sum_g[-1]
        N = len(gap)
        for ii in range(1, N):
            tmp = (
                (sum_g[-1] - sum_g[ii + 1])
                - (num_g[-1] - num_g[ii + 1]) * gap[ii]
                - (sum_g[ii] - num_g[ii] * gap[ii])
            )
            # print(tmp)
            res = min(tmp, res)
        return res
