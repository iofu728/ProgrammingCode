# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-17 11:46:47
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-17 11:47:27

"""


6072. 转角路径的乘积中最多能有几个尾随零 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个二维整数数组 grid ，大小为 m x n，其中每个单元格都含一个正整数。

转角路径 定义为：包含至多一个弯的一组相邻单元。具体而言，路径应该完全 向水平方向 或者 向竖直方向 移动过弯（如果存在弯），而不能访问之前访问过的单元格。在过弯之后，路径应当完全朝 另一个 方向行进：如果之前是向水平方向，那么就应该变为向竖直方向；反之亦然。当然，同样不能访问之前已经访问过的单元格。

一条路径的 乘积 定义为：路径上所有值的乘积。

请你从 grid 中找出一条乘积中尾随零数目最多的转角路径，并返回该路径中尾随零的数目。

注意：

水平 移动是指向左或右移动。
竖直 移动是指向上或下移动。
 

示例 1：



输入：grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
输出：3
解释：左侧的图展示了一条有效的转角路径。
其乘积为 15 * 20 * 6 * 1 * 10 = 18000 ，共计 3 个尾随零。
可以证明在这条转角路径的乘积中尾随零数目最多。

中间的图不是一条有效的转角路径，因为它有不止一个弯。
右侧的图也不是一条有效的转角路径，因为它需要重复访问已经访问过的单元格。
示例 2：



输入：grid = [[4,3,2],[7,6,1],[8,8,8]]
输出：0
解释：网格如上图所示。
不存在乘积含尾随零的转角路径。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= grid[i][j] <= 1000
"""
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def get_num(k, n):
            res = 0
            while k % n == 0:
                k //= n
                res += 1
            return res
            
        N, M = len(grid), len(grid[0])
        num2 = [[get_num(grid[ii][jj], 2) for jj in range(M)] for ii in range(N)]
        num5 = [[get_num(grid[ii][jj], 5) for jj in range(M)] for ii in range(N)]
        x2, x5 = [[0] * M for ii in range(N)], [[0] * M for ii in range(N)]
        y2, y5 = [[0] * M for ii in range(N)], [[0] * M for ii in range(N)]
        for ii in range(N):
            for jj in range(M):
                if ii == 0:
                    x2[ii][jj] = num2[ii][jj]
                    x5[ii][jj] = num5[ii][jj]
                else:
                    x2[ii][jj] = num2[ii][jj] + x2[ii - 1][jj]
                    x5[ii][jj] = num5[ii][jj] + x5[ii - 1][jj]
                if jj == 0:
                    y2[ii][jj] = num2[ii][jj]
                    y5[ii][jj] = num5[ii][jj]
                else:
                    y2[ii][jj] = num2[ii][jj] + y2[ii][jj - 1]
                    y5[ii][jj] = num5[ii][jj] + y5[ii][jj - 1]
        # print(x2)
        res = 0
        for ii in range(N):
            for jj in range(M):
                c = [(x2[ii][jj], x5[ii][jj]), (y2[ii][jj], y5[ii][jj]), (x2[-1][jj] - x2[ii][jj] + num2[ii][jj], x5[-1][jj] - x5[ii][jj] + num5[ii][jj]), (y2[ii][-1] - y2[ii][jj] + num2[ii][jj], y5[ii][-1] - y5[ii][jj] + num5[ii][jj])]
                # print(c)
                for k, q in [(0, 1), (1, 2), (2, 3), (3, 0)]:
                    w2, w5 = c[k][0] + c[q][0] - num2[ii][jj], c[k][1] + c[q][1] - num5[ii][jj]
                    # print(ii, jj, w2, w5)
                    res = max(res, min(w2, w5))
        return res
                
                    
                    
        