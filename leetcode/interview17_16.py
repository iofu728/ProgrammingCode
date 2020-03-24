# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-24 18:50:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-24 19:09:14

"""
面试题 17.16. The Masseuse LCCI
A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept. She needs a break between appointments and therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appoint­ ment requests, find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.

Note: This problem is slightly different from the original one in the book.

## Example 1:

Input:  [1,2,3,1]
Output:  4
Explanation:  Accept request 1 and 3, total minutes = 1 + 3 = 4

## Example 2:

Input:  [2,7,9,3,1]
Output:  12
Explanation:  Accept request 1, 3 and 5, total minutes = 2 + 9 + 1 = 12

## Example 3:

Input:  [2,1,4,5,3,1,1,3]
Output:  12
Explanation:  Accept request 1, 3, 5 and 8, total minutes = 2 + 4 + 3 + 3 = 12
通过次数16,508提交次数30,916
"""
class Solution:
    def massage(self, nums: List[int]) -> int:
        N = len(nums)
        if not N:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(N)]
        dp[0][1] = nums[0]
        for ii in range(1, N):
            dp[ii][0] = max(dp[ii - 1])
            dp[ii][1] = dp[ii - 1][0] + nums[ii]
        return max(dp[N - 1])