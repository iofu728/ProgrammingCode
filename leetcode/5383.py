# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-12 11:14:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-12 11:15:13

"""
5383. Number of Ways to Paint N × 3 Grid
User Accepted:441
User Tried:489
Total Accepted:455
Total Submissions:616
Difficulty:Hard
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214

Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""


class Solution:
    MOD = 10 ** 9 + 7

    def numOfWays(self, n: int) -> int:
        same, diff = 2, 2
        same_ratio, diff_ratio = 5, 4
        same_same, diff_same = 3, 2
        while n > 1:
            t1 = (same * same_same) + (diff * diff_same)
            t2 = (same * (same_ratio - same_same)) + (diff * (diff_ratio - diff_same))
            same, diff = t1, t2
            n -= 1
        return (same + diff) * 3 % self.MOD
