# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-31 23:19:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-31 23:21:44

"""
153. Find Minimum in Rotated Sorted Array Medium
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
Accepted 456,554 Submissions 1,013,032
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        ll, rr = nums[0], nums[-1]
        if ll < rr:
            return ll
        left, right = 0, N - 1
        while left < right - 1:
            mid = (left + right) // 2
            print(left, right, mid)
            if mid == left or mid == right:
                print(mid, right)
                left = right if nums[left] > ll else left
                break
            if nums[mid] > ll:
                left = mid
            else:
                right = mid
        if nums[left] >= ll:
            return nums[right]
        return nums[left]
