# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-30 22:07:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-30 22:08:06

"""
1092. Shortest Common Supersequence Hard
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

## Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

## Note:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
Accepted 8,534 Submissions 16,702
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)
        dp = [["" for _ in range(M + 1)] for _ in range(N + 1)]
        for jj in range(1, M + 1):
            for ii in range(1, N + 1):
                if str1[ii - 1] == str2[jj - 1]:
                    dp[ii][jj] = dp[ii - 1][jj - 1] + str1[ii - 1]
                else:
                    dp[ii][jj] = max(
                        dp[ii - 1][jj], dp[ii][jj - 1], key=lambda i: len(i)
                    )
        result, left, right = "", 0, 0
        for ii in dp[N][M]:
            while left < N and str1[left] != ii:
                result += str1[left]
                left += 1
            while right < M and str2[right] != ii:
                result += str2[right]
                right += 1
            result += ii
            left, right = left + 1, right + 1
        result += str1[left:]
        result += str2[right:]
        # print(dp)
        return result
