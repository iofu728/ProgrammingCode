# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-14 22:18:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-14 22:19:09

"""
139. Word Break Medium
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
Accepted 597,964 Submissions 1,480,067
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        for ii in range(N):
            for jj in range(ii + 1, N + 1):
                if dp[ii] and s[ii:jj] in wordDict:
                    dp[jj] = True
        return dp[-1]
