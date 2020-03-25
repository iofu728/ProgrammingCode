# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-25 13:40:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-25 13:41:54

"""
238. Product of Array Except Self Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

## Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

## Note: Please solve it without division and in O(n).

## Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Accepted 405,753 Submissions 688,993
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1] * len(nums)
        for ii in nums[:-1]:
            left.append(left[-1] * ii)
        for ii in range(len(nums) - 1, 0, -1):
            right[ii - 1] = right[ii] * nums[ii]
        return [ii * jj for ii, jj in zip(left, right)]
