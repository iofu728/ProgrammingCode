# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-14 21:02:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-14 21:03:00

"""
377. Combination Sum IV Medium
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Accepted 132,617 Submissions 291,601
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for ii in range(1, target + 1):
            for num in nums:
                if ii >= num:
                    dp[ii] += dp[ii - num]
        return dp[target]
