# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-04 14:13:52
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-04 14:14:06

"""
6472. 查询后矩阵的和 显示英文描述 
通过的用户数5
尝试过的用户数10
用户总通过次数5
用户总提交次数12
题目难度Medium
给你一个整数 n 和一个下标从 0 开始的 二维数组 queries ，其中 queries[i] = [typei, indexi, vali] 。

一开始，给你一个下标从 0 开始的 n x n 矩阵，所有元素均为 0 。每一个查询，你需要执行以下操作之一：

如果 typei == 0 ，将第 indexi 行的元素全部修改为 vali ，覆盖任何之前的值。
如果 typei == 1 ，将第 indexi 列的元素全部修改为 vali ，覆盖任何之前的值。
请你执行完所有查询以后，返回矩阵中所有整数的和。

 

示例 1：



输入：n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
输出：23
解释：上图展示了每个查询以后矩阵的值。所有操作执行完以后，矩阵元素之和为 23 。
示例 2：



输入：n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
输出：17
解释：上图展示了每一个查询操作之后的矩阵。所有操作执行完以后，矩阵元素之和为 17 。
 

提示：

1 <= n <= 104
1 <= queries.length <= 5 * 104
queries[i].length == 3
0 <= typei <= 1
0 <= indexi < n
0 <= vali <= 105
"""
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        res = 0
        xs, ys = 0, 0
        x_done, y_done = [0] * n, [0] * n
        for t, i, v in queries[::-1]:
            if t == 0:
                if x_done[i] == 1:
                    continue
                res += (n - ys) * v
                xs += 1
                x_done[i] = 1
            else:
                if y_done[i] == 1:
                    continue
                res += (n - xs) * v
                ys += 1
                y_done[i] = 1

        return res
                
            
                
            

        