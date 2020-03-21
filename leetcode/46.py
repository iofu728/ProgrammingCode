# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 19:30:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 19:41:15

"""
46. Permutations Medium

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Accepted 530,197 Submissions 873,567
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backup(nums: List[int], temp: List[int]):
            if not len(nums):
                result.append(temp)
            for idx in range(len(nums)):
                backup(nums[:idx] + nums[idx + 1 :], temp + [nums[idx]])

        backup(nums, [])
        return result
