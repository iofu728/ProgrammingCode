# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-04 10:35:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-04 10:35:44

"""
45. Jump Game II Hard
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

Accepted 240,774 Submissions 801,261
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        res, end, p = 0, 0, 0
        for ii in range(N - 1):
            p = max(nums[ii] + ii, p)
            if ii == end:
                end = p
                res += 1
        return res
