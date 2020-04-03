# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 11:10:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 11:11:59

"""
136. Single Number Easy
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

## Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## Example 1:
Input: [2,2,1]
Output: 1

## Example 2:
Input: [4,1,2,1,2]
Output: 4

Accepted 735,822 Submissions 1,140,916
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for ii in nums:
            a ^= ii
        return a
