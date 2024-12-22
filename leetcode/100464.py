# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-12-22 14:37:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-12-22 14:37:42

"""
100464. 执行操作后不同元素的最大数量 显示英文描述 
通过的用户数20
尝试过的用户数31
用户总通过次数20
用户总提交次数40
题目难度Medium
给你一个整数数组 nums 和一个整数 k。

你可以对数组中的每个元素 最多 执行 一次 以下操作：

将一个在范围 [-k, k] 内的整数加到该元素上。
返回执行这些操作后，nums 中可能拥有的不同元素的 最大 数量。

 

示例 1：

输入： nums = [1,2,2,3,3,4], k = 2

输出： 6

解释：

对前四个元素执行操作，nums 变为 [-1, 0, 1, 2, 3, 4]，可以获得 6 个不同的元素。

示例 2：

输入： nums = [4,4,4,4], k = 1

输出： 3

解释：

对 nums[0] 加 -1，以及对 nums[1] 加 1，nums 变为 [3, 5, 4, 4]，可以获得 3 个不同的元素。

 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
"""
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        changing = [(ii - k, ii + k) for ii in nums]
        last = -inf
        res = 0
        changing = sorted(changing, key=lambda i:i[1])
        for x, y in changing:
            if x > last:
                last = x
                res += 1
            elif y >= last + 1:
                last += 1
                res += 1
        return res
        