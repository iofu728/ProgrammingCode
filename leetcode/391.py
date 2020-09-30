# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 20:33:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 20:35:32

"""
391. Perfect Rectangle Hard
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
 

Accepted 26,538 Submissions 86,659
"""


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        N = len(rectangles)
        points, S = set(), 0
        for x1, y1, x2, y2 in rectangles:
            S += (x2 - x1) * (y2 - y1)
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)
        points = sorted(points)
        if not len(points):
            return False

        x1, y1 = points[0]
        x2, y2 = points[-1]
        if len(points) != 4:
            return False
        new_S = (x2 - x1) * (y2 - y1)
        if new_S != S:
            return False
        return True

