# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 15:37:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 16:21:01

"""
673. Number of Longest Increasing Subsequence Medium
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

Accepted 53,402 Submissions 149,176
"""
from collections import defaultdict


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if not N:
            return 0
        dp, total = [], []
        for num in nums:
            index = len(dp) - 1
            if not dp or num > dp[-1]:
                dp.append(num)
                total.append(defaultdict(int))
            else:
                while index >= 0 and dp[index] >= num:
                    index -= 1
                dp[index + 1] = num
            if index + 1 == 0:
                total[index + 1][num] += 1
            else:
                # print(index, total)
                total[index + 1][num] += sum(
                    [v for k, v in total[index].items() if k < num]
                )
        return sum(total[-1].values())
