# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-25 01:01:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-25 01:03:48

"""
410. Split Array Largest Sum Hard
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Accepted 91,811 Submissions 206,580
"""
class Solution:
    MAX = 10 ** 19 + 7

    def splitArray(self, nums: List[int], m: int) -> int:
        N = len(nums)
        dp = [[self.MAX] * (m + 1) for _ in range(N + 1)]
        sub = [0]
        for ii in nums:
            sub.append(sub[-1] + ii)
        dp[0][0] = 0
        for ii in range(1, N + 1):
            for jj in range(1, min(ii, m) + 1):
                for kk in range(ii):
                    dp[ii][jj] = min(dp[ii][jj], max(dp[kk][jj - 1], sub[ii] - sub[kk]))
        return dp[N][m]
