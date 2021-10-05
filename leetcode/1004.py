# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-05 19:23:08
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-05 19:23:33

"""
1004. Max Consecutive Ones III
Medium

3223

45

Add to List

Share
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
Accepted
149,859
Submissions
243,998
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left, lsum, rsum = 0, 0, 0
        res = 0
        for ii in range(N):
            rsum += 1 - nums[ii]
            while lsum < rsum - k:
                lsum += 1 - nums[left]
                left += 1
            res = max(res, ii - left + 1)
        return res
