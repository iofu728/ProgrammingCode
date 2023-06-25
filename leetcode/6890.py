# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-25 10:18:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-25 10:18:40

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = float("inf")
        for ii in range(1, len(nums)):
            a, b = nums[ii - 1], nums[ii]
            res = min((b - a), res)
        return res