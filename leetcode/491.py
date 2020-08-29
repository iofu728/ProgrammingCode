# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-26 00:53:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-26 00:56:30

"""
491. Increasing Subsequences Medium
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Constraints:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
Accepted 48,878 Submissions 105,582
"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        if not N:
            return []
        pres = {(nums[0],)}
        for ii in nums[1:]:
            # print(pres)
            pres.update({jj + (ii,) for jj in pres if jj[-1] <= ii})
            pres.add((ii,))
        # print(pres)
        return [list(ii) for ii in pres if len(ii) > 1]
