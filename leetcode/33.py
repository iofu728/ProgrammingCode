# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 17:01:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 17:41:49

"""
33. Search in Rotated Sorted Array
Medium

3925

407

Add to List

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Accepted
593,501
Submissions
1,763,250
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        M = len(nums)
        left, right = 0, M - 1
        while left < right and left < M - 1 and right > 0:
            L, R = nums[left], nums[right]
            if L == target:
                return left
            elif R == target:
                return right
            middle = int((left + right) / 2)
            T = nums[middle]
            if T == target:
                return middle
            if middle == left or middle == right:
                return -1
            if L > R:
                if L > target and R < target:
                    return -1
                if L < target:
                    if T < R or T > target:
                        right = middle
                    else:
                        left = middle
                if R > target:
                    if T > L or T < target:
                        left = middle
                    else:
                        right = middle
            else:
                if T > target:
                    right = middle
                else:
                    left = middle
        if left < M and nums[left] == target:
            return left
        elif right >= 0 and nums[right] == target:
            return right
        return -1
