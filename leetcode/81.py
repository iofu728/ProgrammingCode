# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-01 12:22:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-01 12:23:55

"""
81. Search in Rotated Sorted Array II Medium
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
Accepted 254,913 Submissions 771,847
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left += 1
            elif nums[left] < nums[mid]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
