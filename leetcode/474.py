# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-14 23:32:38
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-14 23:33:13

"""
474. Ones and Zeroes Medium
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
Accepted 51,874 Submissions 120,639
"""
from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dp[0][0] = 1
        for ii in strs:
            # print(dp)
            c = Counter(ii)
            c1, c2 = c["0"], c["1"]
            for jj in range(m, c1 - 1, -1):
                for kk in range(n, c2 - 1, -1):
                    dp[jj][kk] = max(1 + dp[jj - c1][kk - c2], dp[jj][kk])
        return dp[-1][-1]
