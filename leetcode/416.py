# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-11 01:44:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-11 01:45:43

"""
416. Partition Equal Subset Sum Medium
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

Accepted 147,928 Submissions 347,179
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N, S = len(nums), sum(nums)

        if S >> 1 << 1 != S:
            return False

        bag = S // 2
        dp = [-1] * (bag + 1)
        for ii in range(bag + 1):
            dp[ii] = nums[0] == ii

        for ii in range(1, N):
            for jj in range(bag, -1, -1):
                if jj < nums[ii]:
                    break
                dp[jj] = dp[jj] or dp[jj - nums[ii]]
        return dp[-1]
