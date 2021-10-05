# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-05 19:54:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-05 19:55:29

"""
1262. Greatest Sum Divisible by Three
Medium

938

28

Add to List

Share
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

 

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
Accepted
32,885
Submissions
65,043
"""


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res = sum(nums)
        a = res % 3
        if a == 0:
            return res
        dp_1 = sorted([i for i in nums if i % 3 == 1])[:2]
        dp_2 = sorted([i for i in nums if i % 3 == 2])[:2]
        if a == 1:
            if dp_1:
                if len(dp_2) == 2:
                    return res - min(sum(dp_2), dp_1[0])
                return res - dp_1[0]
            if len(dp_2) == 2:
                return res - sum(dp_2)
            return 0
        if dp_2:
            if len(dp_1) == 2:
                return res - min(sum(dp_1), dp_2[0])
            return res - dp_2[0]
        if len(dp_1) == 2:
            return res - sum(dp_1)
        return 0
