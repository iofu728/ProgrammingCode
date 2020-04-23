# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-17 12:17:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-17 12:42:07

"""
55. Jump Game Medium
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
Accepted 384,907 Submissions 1,151,690
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        N, r = len(nums), 0
        for ii in range(N):
            if ii <= r:
                r = max(ii + nums[ii], r)
                if r >= N - 1:
                    return True
        return False
