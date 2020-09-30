# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-30 23:40:58
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-30 23:48:27

"""
792. Number of Matching Subsequences Medium
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
Accepted 45,477 Submissions 95,274
"""
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        needs = defaultdict(list)
        for ii in words:
            needs[ii[0]].append(ii[1:])
        res = 0
        for s in S:
            if s not in needs:
                continue
            tmp = needs[s]
            needs[s] = []
            for jj in tmp:
                if jj == "":
                    res += 1
                else:
                    needs[jj[0]].append(jj[1:])
        return res

