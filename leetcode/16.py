# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 16:33:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 17:00:32

"""
16. 3Sum Closest
Medium

1703

121

Add to List

Share
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Accepted
431,704
Submissions
944,380
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet_sum = target + 999999999
        nums = sorted(nums)
        M = len(nums)
        for ii in range(M):
            if nums[ii] > target and (
                abs(nums[ii] - target) > abs(target - closet_sum)
            ):
                continue
            if ii > 0 and nums[ii - 1] == nums[ii]:
                continue
            jj, kk = ii + 1, M - 1
            while jj < kk and jj < M and kk > ii:
                temp_sum = nums[ii] + nums[jj] + nums[kk]
                if abs(temp_sum - target) < abs(target - closet_sum):
                    closet_sum = temp_sum
                if temp_sum == target:
                    return temp_sum
                elif temp_sum > target:
                    kk -= 1
                else:
                    jj += 1
        return closet_sum
