# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-14 14:45:08
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-14 14:45:51

"""
1401. Circle and Rectangle Overlapping Medium
Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there are any point (xi, yi) such that belongs to the circle and the rectangle at the same time.

 

Example 1:



Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0) 
Example 2:



Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true
Example 3:



Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
Output: true
Example 4:

Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
 

Constraints:

1 <= radius <= 2000
-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
x1 < x2
y1 < y2
Accepted 5,910 Submissions 14,026
"""


class Solution:
    def checkOverlap(
        self,
        radius: int,
        x_center: int,
        y_center: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True
        if x_center > x2 and y1 <= y_center <= y2:
            return radius >= x_center - x2
        if y_center < y1 and x1 <= x_center <= x2:
            return radius >= y1 - y_center
        if x_center < x1 and y1 <= y_center <= y2:
            return radius >= x1 - x_center
        if y_center > y2 and x1 <= x_center <= x2:
            return radius >= y_center - y2
        return (
            min(
                (x1 - x_center) ** 2 + (y2 - y_center) ** 2,
                (x2 - x_center) ** 2 + (y2 - y_center) ** 2,
                (x2 - x_center) ** 2 + (y1 - y_center) ** 2,
                (x1 - x_center) ** 2 + (y1 - y_center) ** 2,
            )
            < radius ** 2
        )
