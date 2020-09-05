# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-05 00:48:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-05 00:49:25

"""
60. Permutation Sequence Hard
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Accepted 207,752 Submissions 538,422
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        dp = [1]
        for ii in range(1, n):
            dp.append(dp[-1] * ii)
        k -= 1
        res, flag = [], [1] * (n + 1)
        for ii in range(1, n + 1):
            order = k // dp[n - ii] + 1
            for jj in range(1, n + 1):
                order -= flag[jj]
                if order == 0:
                    res.append(str(jj))
                    flag[jj] = 0
                    break
            k %= dp[n - ii]
        return "".join(res)
