# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-22 14:00:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-22 14:00:23

"""
1510. Stone Game IV
Hard

705

34

Add to List

Share
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
 

Constraints:

1 <= n <= 105
Accepted
37,856
Submissions
62,594
"""
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(x):
            if x == 0:
                return False
            for ii in range(1, int(math.sqrt(x)) + 1):
                if not dfs(x - ii ** 2):
                    return True
            return False
        return dfs(n)
