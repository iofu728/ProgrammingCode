# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-16 10:18:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-16 11:45:38

"""
56. Merge Intervals Medium
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Accepted 534,213 Submissions 1,395,151
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        if not N:
            return intervals
        intervals = sorted(intervals)
        res = [intervals[0]]
        for ii in intervals[1:]:
            last_e = res[-1][1]
            if last_e >= ii[0]:
                res[-1][1] = max(ii[1], last_e)
            else:
                res.append(ii)
        return res
