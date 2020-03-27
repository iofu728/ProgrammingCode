# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-27 13:08:33
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-27 13:17:40

"""
300. Longest Increasing Subsequence Medium

Given an unsorted array of integers, find the length of longest increasing subsequence.

## Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

## Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

Accepted 326,067 Submissions 776,061
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        for ii in range(1, N):
            tt = [dp[jj] for jj in range(ii) if nums[jj] < nums[ii]]
            if len(tt):
                dp[ii] = max(tt) + 1
        return max(dp) if N else 0
