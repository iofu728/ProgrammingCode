# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-17 11:33:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-17 11:34:40

"""
18. 4Sum Medium
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
Accepted 308,366 Submissions 939,543
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.nSum(nums, target, 4)

    def nSum(self, nums: List[int], target: int, n: int) -> List[List[int]]:
        N, res = len(nums), []
        nums = sorted(nums)

        def dfs(pos: int, cur: List[int], n: int, target: int):
            if n == 2:
                left, right = pos, N - 1
                while left < right:
                    now = nums[left] + nums[right]
                    if now < target:
                        left += 1
                    elif now > target:
                        right -= 1
                    else:
                        res.append(cur + [nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left, right = left + 1, right - 1
                return
            left = pos
            while left < N - n + 1:
                if nums[left] * n > target or nums[-1] * n < target:
                    break
                if left > pos and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                dfs(left + 1, cur + [nums[left]], n - 1, target - nums[left])
                left += 1

        dfs(0, [], n, target)
        return res
