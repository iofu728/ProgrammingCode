# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-12 22:40:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-12 22:40:42

"""
面试题 16.03. Intersection LCCI
Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any. If there's no intersection, return an empty array.

The absolute error should not exceed 10^-6. If there are more than one intersections, return the one with smallest X axis value. If there are more than one intersections that have same X axis value, return the one with smallest Y axis value.
Example 1:

Input: 
line1 = {0, 0}, {1, 0}
line2 = {1, 1}, {0, -1}
Output:  {0.5, 0}
Example 2:

Input: 
line1 = {0, 0}, {3, 3}
line2 = {1, 1}, {2, 2}
Output:  {1, 1}
Example 3:

Input: 
line1 = {0, 0}, {1, 1}
line2 = {1, 0}, {2, 1}
Output:  {}  (no intersection)
Note:

The absolute value of coordinate value will not exceed 2^7.
All coordinates are valid 2D coordinates.
通过次数5,902提交次数12,573
"""


class Solution:
    def intersection(
        self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]
    ) -> List[float]:
        start1, end1 = sorted([start1, end1], key=lambda i: i)
        start2, end2 = sorted([start2, end2], key=lambda i: i)
        if start1 > start2:
            start1, end1, start2, end2 = start2, end2, start1, end1
        b1, a1 = [ii - jj for ii, jj in zip(start1, end1)]
        b2, a2 = [ii - jj for ii, jj in zip(start2, end2)]
        b1, b2 = -b1, -b2
        t = b2 * a1 - b1 * a2
        tt = (
            b1 * b2 * (start1[1] - start2[1])
            + start1[0] * b2 * a1
            - start2[0] * b1 * a2
        )
        if not t:
            if (
                tt
                or (end1[0] < start2[0])
                or (start1[0] == end1[0] == start2[0] and end1[1] < start2[1])
            ):
                return []
            return start2
        x = tt / (t)
        if (x - start1[0]) * (x - end1[0]) > 0 or (x - start2[0]) * (x - end2[0]) > 0:
            return []
        if b1:
            y = a1 * (start1[0] - x) / b1 + start1[1]
        else:
            y = a2 * (start2[0] - x) / b2 + start2[1]
        return [x, y]
