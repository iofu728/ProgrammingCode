# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 15:27:45
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 16:02:39

"""
525. Contiguous Array Medium
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

## Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

## Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

Accepted 56,593 Submissions 126,000
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N, count, t, max_len = len(nums), {}, 0, 0
        count[0] = -1
        for idx, ii in enumerate(nums):
            t += 1 if ii else -1
            if t in count:
                # print(t, idx, count[t])
                max_len = max(max_len, idx - count[t])
            else:
                count[t] = idx
        # print(count)
        return max_len
