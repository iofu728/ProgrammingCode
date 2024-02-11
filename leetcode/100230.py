# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-02-11 11:07:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-02-11 11:07:40

"""
100230. 修改矩阵 显示英文描述 
通过的用户数283
尝试过的用户数294
用户总通过次数283
用户总提交次数304
题目难度Easy
给你一个下标从 0 开始、大小为 m x n 的整数矩阵 matrix ，新建一个下标从 0 开始、名为 answer 的矩阵。使 answer 与 matrix 相等，接着将其中每个值为 -1 的元素替换为所在列的 最大 元素。

返回矩阵 answer 。

 

示例 1：


输入：matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
输出：[[1,2,9],[4,8,6],[7,8,9]]
解释：上图显示了发生替换的元素（蓝色区域）。
- 将单元格 [1][1] 中的值替换为列 1 中的最大值 8 。
- 将单元格 [0][2] 中的值替换为列 2 中的最大值 9 。
示例 2：


输入：matrix = [[3,-1],[5,2]]
输出：[[3,2],[5,2]]
解释：上图显示了发生替换的元素（蓝色区域）。
 

提示：

m == matrix.length
n == matrix[i].length
2 <= m, n <= 50
-1 <= matrix[i][j] <= 100
测试用例中生成的输入满足每列至少包含一个非负整数。
"""
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        N, M = len(matrix), len(matrix[0])
        for jj in range(M):
            y = max([matrix[ii][jj] for ii in range(N)])
            for ii in range(N):
                if matrix[ii][jj] == -1:
                    matrix[ii][jj] = y
        return matrix