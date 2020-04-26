# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-26 13:32:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-26 13:36:09

"""
5394. 对角线遍历 II 显示英文描述 
通过的用户数462
尝试过的用户数1065
用户总通过次数465
用户总提交次数2179
题目难度Medium
给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。

示例 1：
输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,4,2,7,5,3,8,6,9]

示例 2：
输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

示例 3：
输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
输出：[1,4,2,5,3,8,6,9,7,10,11]

示例 4：
输入：nums = [[1,2,3,4,5,6]]
输出：[1,2,3,4,5,6]

提示：

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
nums 中最多有 10^5 个数字。
"""


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        pre, res, N = [(0, 0)], [nums[0][0]], len(nums)
        while pre:
            now = []
            for i, j in pre:
                for ii, jj in (i + 1, j), (i, j + 1):
                    if ii < N and jj < len(nums[ii]) and nums[ii][jj] != -1:
                        res.append(nums[ii][jj])
                        now.append((ii, jj))
                        nums[ii][jj] = -1
            pre = now
        return res
