# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 20:09:30
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 20:13:36

"""
260. Single Number III Medium
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

1 <= nums.length <= 30000
 Each integer in nums will appear twice, only two integers will appear once.
Accepted 173,123 Submissions 267,528
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        N = len(nums)
        a = 0
        for ii in nums:
            a ^= ii
        b = a & (-a)
        x = 0
        for ii in nums:
            if ii & b:
                x ^= ii
        return [x, a ^ x]
