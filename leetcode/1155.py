# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-12-22 20:54:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-12-22 20:57:01

"""
1155. Number of Dice Rolls With Target Sum Medium
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
Accepted 57,942 Submissions121,839
"""
class Solution:
    MODS = 10 ** 9 + 7
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * target for _ in range(d)]
        for ii in range(min(f, target)):
            dp[0][ii] = 1
        for ii in range(1, d):
            for jj in range(1 * (ii + 1)  - 1, min((f) * (ii + 1), target)):
                dp[ii][jj] = sum([dp[ii - 1][kk] for kk in range(max(jj -  f, 0),  jj)]) % self.MODS
        return dp[d - 1][target - 1] % self.MODS