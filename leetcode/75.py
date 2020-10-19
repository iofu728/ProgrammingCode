# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-07 13:54:25
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-07 13:55:53

"""
75. Sort Colors Medium
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
Accepted 564,576 Submissions 1,176,335
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        p0, p1 = 0, 0
        for ii in range(N):
            if nums[ii] == 1:
                nums[ii], nums[p1] = nums[p1], nums[ii]
                p1 += 1
            elif nums[ii] == 0:
                nums[ii], nums[p0] = nums[p0], nums[ii]
                if nums[ii] == 1:
                    nums[ii], nums[p1] = nums[p1], nums[ii]
                p0 += 1
                p1 += 1
