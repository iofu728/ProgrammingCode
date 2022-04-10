# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-09 13:47:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-09 13:47:54

"""
780. Reaching Points
Hard

932

161

Add to List

Share
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

 

Example 1:

Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
Example 2:

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false
Example 3:

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true
 

Constraints:

1 <= sx, sy, tx, ty <= 109
Accepted
41,160
Submissions
130,467
"""

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        x, y = tx, ty
        while x > 0 and y > 0:
            if x == sx and y == sy:
                return True
            if x > y:
                if y == sy and sx >= sy:
                    k = min((sx - x % y - 1) // y + 1, (x - x % y) // y)
                    dx, dy = x % y + y * k, y
                    if dx == x:
                        x = dx - y
                    else:
                        x = dx
                else:
                    x, y = x % y, y
            else:
                if x == sx and sy >= sx:
                    k = min((sy - y % x - 1) // x + 1, (y - y % x) // x)
                    dx, dy = x, y % x + x * k
                    # print(dx, dy, 11)
                    if dy == y:
                        y = dy - x
                    else:
                        y = dy
                else:
                    x, y = x, y % x
            # print(x, y)
        return False