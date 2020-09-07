# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 14:14:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-07 14:15:33

"""
327. Count of Range Sum Hard
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
 

Constraints:

0 <= nums.length <= 10^4
Accepted 44,184 Submissions 125,061
"""
import bisect


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        N, prefix, sums, pre, res = len(nums), [0], [], 0, 0
        if not N:
            return 0
        for ii in nums:
            pre += ii
            left = bisect.bisect_left(prefix, pre - upper)
            right = bisect.bisect_right(prefix, pre - lower)
            res += right - left
            bisect.insort(prefix, pre)
        return res
