# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-30 21:44:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-30 21:45:35

"""
452. Minimum Number of Arrows to Burst Balloons Medium
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

Accepted 66,749 Submissions 134,877
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        N = len(points)
        if N <= 1:
            return N
        points = sorted(points, key=lambda i: i[0])
        res, end = 1, points[0][1]
        # print(points)
        for ii, jj in points[1:]:
            if ii <= end:
                end = min(jj, end)
            else:
                res += 1
                end = jj
        return res
