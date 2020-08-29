# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-29 21:13:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-29 21:14:08

"""
464. Can I Win Medium
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise return false. Assume both players play optimally.

Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true
Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true

Constraints:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
Accepted 52,718 Submissions 182,764
"""
from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def dfs(state: int, d: int):
            for ii in range(maxChoosableInteger - 1, -1, -1):
                if not state & (1 << ii):
                    if ii + 1 >= d or not dfs(state + (1 << ii), d - ii - 1):
                        return True
            return False

        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        return dfs(0, desiredTotal)

