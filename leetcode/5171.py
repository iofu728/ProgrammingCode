# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-02-23 11:47:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-02-23 11:48:19
"""
5171. Closest Divisors
User Accepted:2368
User Tried:2841
Total Accepted:2397
Total Submissions:4760
Difficulty:Medium
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

 

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]
 

Constraints:

1 <= num <= 10^9
"""
import math


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a, b = self.get_middle_factor(num + 1)
        c, d = self.get_middle_factor(num + 2)
        if b - a < d - c:
            return a, b
        return c, d

    def get_middle_factor(self, num: int) -> int:
        for ii in range(int(math.sqrt(num)), 1, -1):
            if num % ii == 0:
                return ii, int(num // ii)
        return 1, num
