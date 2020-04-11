# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-11 10:56:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-11 10:57:24

"""
494. Target Sum Medium
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
Accepted 142,079 Submissions 305,629
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        N = len(nums)
        dp = [[0] * 2001 for _ in range(N)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for ii in range(1, N):
            for jj in range(-1000, 1001):
                if dp[ii - 1][jj + 1000] > 0:
                    dp[ii][jj + nums[ii] + 1000] += dp[ii - 1][jj + 1000]
                    dp[ii][jj - nums[ii] + 1000] += dp[ii - 1][jj + 1000]
        return 0 if S > 1000 else dp[N - 1][S + 1000]
