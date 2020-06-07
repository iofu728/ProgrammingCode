# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-06-07 10:30:16
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-06-07 10:35:49

"""
5428. 重新排列数组 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

 

示例 1：

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
示例 2：

输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]
示例 3：

输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]
 

提示：

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for idx, ii in enumerate(nums):
            if idx >> 1 << 1 == idx:
                tid = (idx) // 2
            else:
                tid = n + (idx // 2)
            res.append(nums[tid])
        return res
