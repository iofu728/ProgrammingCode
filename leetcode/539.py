# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-18 19:50:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-18 19:51:12

"""
539. Minimum Time Difference
Medium

850

187

Add to List

Share
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints <= 2 * 104
timePoints[i] is in the format "HH:MM".
Accepted
71,400
Submissions
134,099
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def str2num(t):
            h, r = t.split(":")
            h, r = int(h), int(r)
            return h * 60 + r
        s = sorted([str2num(ii) for ii in timePoints])
        N = len(timePoints)
        return min([s[ii + 1] - s[ii] for ii in range(N - 1)] + [24 * 60 + s[0] - s[-1]])