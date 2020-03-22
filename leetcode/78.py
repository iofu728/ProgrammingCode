# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-22 19:20:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-22 19:26:03

"""
78. Subsets Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

## Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Accepted 496,690 Submissions 851,699
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        M = len(nums)

        def dfs(num: List[int], idx: int):
            if idx == M:
                result.append(num)
                return
            dfs(num, idx + 1)
            dfs(num + [nums[idx]], idx + 1)

        dfs([], 0)
        return result
