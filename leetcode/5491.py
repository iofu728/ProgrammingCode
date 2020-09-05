# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-05 22:30:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-05 22:32:53

"""
5491. 矩阵对角线元素的和 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

 

示例  1：



输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。
示例  2：

输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8
示例 3：

输入：mat = [[5]]
输出：5
 

提示：

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        res = 0
        for left in range(N):
            right = N - 1 - left
            res += mat[left][left]
            if left != right:
                res += mat[left][right]
        return res

