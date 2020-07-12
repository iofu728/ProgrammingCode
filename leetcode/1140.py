# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-12 00:05:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-12 00:27:08

"""
1140. Stone Game II Medium
Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
Accepted 13,537 Submissions 21,561
"""


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N, memory = len(piles), {}
        s = [0] * (N + 1)
        for ii in range(N - 1, -1, -1):
            s[ii] = s[ii + 1] + piles[ii]

        def dfs(i, M):
            if (i, M) in memory:
                return memory[(i, M)]
            if i >= N:
                return 0
            if i + 2 * M >= N:
                return s[i]
            best = 0
            for ii in range(1, 2 * M + 1):
                best = max(best, s[i] - dfs(i + ii, max(ii, M)))
            memory[(i, M)] = best
            return best

        return dfs(0, 1)
