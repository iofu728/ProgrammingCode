# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-10 01:04:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-10 01:06:16

"""
128. Longest Consecutive Sequence Hard
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Accepted 323,677 Submissions 713,922
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        nums_set = set(nums)
        for ii in nums:
            if ii - 1 in nums_set:
                continue
            tmp_num, tmp_len = ii, 1
            while tmp_num + 1 in nums_set:
                tmp_len += 1
                tmp_num += 1
            res = max(tmp_len, res)
        return res
