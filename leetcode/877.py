# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 23:48:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 23:50:16

"""
877. Stone Game Medium
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
Accepted 56,443 Submissions 87,599
"""
from functools import lru_cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            parity = (j - i - N) % 2
            if parity:
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, N - 1) > 0
