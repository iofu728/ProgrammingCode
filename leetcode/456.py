# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-03-24 18:03:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-03-24 18:46:25

"""
456. 132 Pattern
Medium

2194

139

Add to List

Share
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109
Accepted 85,405 Submissions 278,349
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        a2s = [nums[-1]]
        a2 = float("-inf")

        for ii in range(N - 2, -1, -1):
            now = nums[ii]
            if now < a2:
                return True
            while a2s and now > a2s[-1]:
                a2 = a2s[-1]
                a2s.pop()
            if now > a2:
                a2s.append(now)
        return False