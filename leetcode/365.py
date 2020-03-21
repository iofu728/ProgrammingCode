# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-21 13:13:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-21 13:53:06

"""
365. Water and Jug Problem
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
通过次数10,211提交次数31,470
"""


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or (remain_x + remain_y) == z:
                return True
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))
            stack.append((x, remain_y))  # full x
            stack.append((remain_x, y))  # full y
            stack.append((0, remain_y))  # empty x
            stack.append((remain_x, 0))  # empty y
            pour_x = min(remain_x, y - remain_y)
            stack.append((remain_x - pour_x, remain_y + pour_x))  # pour x
            pour_y = min(remain_y, x - remain_x)
            stack.append((remain_x + pour_y, remain_y - pour_y))  # pour y
        return False


"""
ax + by = z

Bézout's identity: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
"""

import math


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x + y:
            return False
        if x == 0 or y == 0:
            return z == 0 or (x + y == z)
        return z % math.gcd(x, y) == 0


def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return b
