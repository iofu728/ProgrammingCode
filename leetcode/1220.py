# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-17 20:16:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-17 20:17:52

"""
1220. Count Vowels Permutation
Hard

875

86

Add to List

Share
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
Accepted
43,473
Submissions
77,162
"""
class Solution:
    # 0 -> 1
    # 1 -> 0, 2
    # 2 -> 0, 1, 3, 4
    # 3 -> 1, 4
    # 4 -> 0
    DIRS = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
    MOD = 10 ** 9 + 7
    def countVowelPermutation(self, n: int) -> int:
        DIRS = [[] for _ in range(5)]
        for ii, jj in enumerate(self.DIRS):
            for kk in jj:
                DIRS[kk].append(ii)
        dp = [1] * 5
        for ii in range(n - 1):
            dp = [sum([dp[jj] for jj in ii]) % self.MOD for ii in DIRS]
            # print(dp)
        return sum(dp) % self.MOD
