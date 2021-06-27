# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-06-27 15:15:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-27 15:15:38

"""
5798. 循环轮转矩阵 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个大小为 m x n 的整数矩阵 grid​​​ ，其中 m 和 n 都是 偶数 ；另给你一个整数 k 。

矩阵由若干层组成，如下图所示，每种颜色代表一层：



矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其 逆时针 方向的相邻元素。轮转示例如下：


返回执行 k 次循环轮转操作后的矩阵。

 

示例 1：


输入：grid = [[40,10],[30,20]], k = 1
输出：[[10,20],[40,30]]
解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
示例 2：

  
输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
 

提示：

m == grid.length
n == grid[i].length
2 <= m, n <= 50
m 和 n 都是 偶数
1 <= grid[i][j] <= 5000
1 <= k <= 109
"""


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def get_kk(k):
            res = []
            for jj in range(k, M - k):
                res.append(grid[k][jj])
            for ii in range(k + 1, N - k):
                res.append(grid[ii][M - k - 1])
            for jj in range(M - k - 2, k - 1, -1):
                res.append(grid[N - k - 1][jj])
            for ii in range(N - k - 2, k, -1):
                res.append(grid[ii][k])
            return res

        def set_kk(k, res):
            for jj in range(k, M - k):
                grid[k][jj] = res.pop(0)
            for ii in range(k + 1, N - k):
                grid[ii][M - k - 1] = res.pop(0)
            for jj in range(M - k - 2, k - 1, -1):
                grid[N - k - 1][jj] = res.pop(0)
            for ii in range(N - k - 2, k, -1):
                grid[ii][k] = res.pop(0)

        N, M = len(grid), len(grid[0])
        K = min(N // 2, M // 2)
        for ii in range(K):
            res = get_kk(ii)
            t = len(res)
            tmp_k = k % t
            res = res[tmp_k:] + res[:tmp_k]
            set_kk(ii, res)
        return grid
