# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 19:33:33
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 19:34:07

"""
154. Find Minimum in Rotated Sorted Array II Hard
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
Accepted 211,001 Submissions 506,856
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        res, left, right, l_v, r_v = nums[0], 0, N - 1, nums[0], nums[-1]
        if l_v < r_v:
            return l_v
        elif l_v == r_v:
            while left < right and nums[left] >= l_v:
                left += 1
            return nums[left]

        while left < right:
            mid = (left + right) // 2
            if mid in [left, right]:
                left = right if nums[mid] < l_v else left
                break
            if nums[mid] >= l_v:
                left = mid
            else:
                right = mid
        # print(left, right)
        if nums[left] >= l_v:
            return nums[right]
        return nums[left]
