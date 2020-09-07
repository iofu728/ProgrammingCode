# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 11:45:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-07 11:46:22

"""
1048. Longest String Chain Medium
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
 

Accepted 71,593 Submissions 130,532
"""
from collections import Counter


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def in_c(a: int, b: int):
            for k, v in a.items():
                if k not in b or b[k] < v:
                    return False
            return True

        N = len(words)
        words = sorted(words, key=lambda i: len(i))
        word_c = [Counter(ii) for ii in words]
        dp = [1] * N
        for ii in range(N):
            can = [
                kk
                for jj, kk, mm in zip(word_c[:ii], dp[:ii], words[:ii])
                if len(words[ii]) == len(mm) + 1 and in_c(jj, word_c[ii])
            ]
            if can:
                dp[ii] = max(can) + 1
        print(words)
        print(dp)
        return max(dp)

