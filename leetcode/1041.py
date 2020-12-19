# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-26 22:51:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-26 22:52:49

"""
1041. Robot Bounded In Circle Medium
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Note:

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
Accepted 41,955 Submissions 77,319
"""


class Solution:
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def isRobotBounded(self, instructions: str) -> bool:
        def once(direction, base, step):
            if step == "L":
                direction = (direction - 1 + 4) % 4
            elif step == "R":
                direction = (direction + 1) % 4
            else:
                dx, dy = self.DIRS[direction]
                base[0] += dx
                base[1] += dy
            return direction, base

        d, b = 0, [0, 0]
        for ii in instructions:
            d, b = once(d, b, ii)
        # print(d, b)
        return d != 0 or b == [0, 0]
