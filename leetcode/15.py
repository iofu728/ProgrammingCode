# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 16:18:33
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 16:32:43

"""
15. 3Sum
Medium

5822

712

Add to List

Share
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
Accepted
802,681
Submissions
3,110,774
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        M = len(nums)
        for ii in range(M):
            if nums[ii] > 0:
                continue
            if ii > 0 and nums[ii - 1] == nums[ii]:
                continue
            jj, kk = ii + 1, M - 1
            while jj < kk and jj < M and kk > ii:
                if nums[ii] + nums[jj] + nums[kk] == 0:
                    if (nums[ii], nums[jj], nums[kk]) not in result:
                        result.add((nums[ii], nums[jj], nums[kk]))
                    while jj < M - 1 and nums[jj + 1] == nums[jj]:
                        jj += 1
                    while kk > ii + 1 and nums[kk - 1] == nums[kk]:
                        kk -= 1
                    kk -= 1
                    jj += 1
                elif nums[ii] + nums[jj] + nums[kk] > 0:
                    kk -= 1
                else:
                    jj += 1
        return [list(ii) for ii in result]
