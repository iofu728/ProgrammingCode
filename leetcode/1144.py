# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-15 19:53:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-15 19:54:01

"""
1144. Decrease Elements To Make Array Zigzag Medium
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.
Example 2:

Input: nums = [9,6,1,6,2]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
Accepted 9,396 Submissions 20,665
"""
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        N = len(nums)
        res1, res2 = 0, 0
        for ii in range(N):
            if ii >> 1 << 1 == ii:
                d1 = (0 if ii == N - 1 or nums[ii + 1] > nums[ii] else nums[ii] - nums[ii + 1] + 1)
                d2 = (0 if ii == 0 or nums[ii] < nums[ii - 1] else nums[ii] - nums[ii - 1] + 1)
                res1 += max(d1, d2)
            else:
                d1 = (0 if ii == N - 1 or nums[ii + 1] > nums[ii] else nums[ii] - nums[ii + 1] + 1)
                d2 = (0 if ii == 0 or nums[ii] < nums[ii - 1] else nums[ii] - nums[ii - 1] + 1)
                res2 += max(d1, d2)
        return min(res1, res2)
