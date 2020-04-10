# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-06 23:32:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-06 23:33:36

"""
72. Edit Distance Hard
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

## Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

## Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Accepted 233,232 Submissions 558,644
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        if N == 0 or M == 0:
            return max(N, M)
        for ii in range(N + 1):
            dp[ii][0] = ii
        for jj in range(M + 1):
            dp[0][jj] = jj
        for ii in range(1, N + 1):
            for jj in range(1, M + 1):
                max_x = dp[ii - 1][jj] + 1
                max_y = dp[ii][jj - 1] + 1
                max_xy = dp[ii - 1][jj - 1]
                if word1[ii - 1] != word2[jj - 1]:
                    max_xy += 1
                dp[ii][jj] = min(max_x, max_y, max_xy)
        return dp[N][M]
