# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-10 22:49:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-10 23:35:16

"""
152. Maximum Product Subarray Medium
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Accepted 300,640 Submissions 969,069
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if not N:
            return
        res, pre_max, pre_min = nums[0], nums[0], nums[0]
        for ii in nums[1:]:
            cur_max = max(pre_max * ii, pre_min * ii, ii)
            cur_min = min(pre_max * ii, pre_min * ii, ii)
            res = max(res, cur_max)
            pre_max, pre_min = cur_max, cur_min
        return res
