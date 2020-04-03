# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 15:24:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 15:25:08


"""
53. Maximum Subarray Easy
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Accepted 818,860 Submissions 1,784,301
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0 for _ in range(N)]
        pre, max_num = 0, -2 ** 32
        for ii in range(N):
            dp[ii] = max(nums[ii], nums[ii] + pre)
            pre = dp[ii]
            if dp[ii] > max_num:
                max_num = dp[ii]
        return max_num
