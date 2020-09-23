# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-23 19:39:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-23 19:42:08

"""
472. Concatenated Words Hard
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
Accepted 71,393 Submissions 161,190
"""


class Solution:
    ENDS = "#"

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(w, idx, c, tree):
            # print(w, idx, c, tree)
            nonlocal res
            if w in res:
                return
            if idx > len(w):
                return
            if idx == len(w):
                if c >= 1 and self.ENDS in tree:
                    res.add(w)
                return
            if self.ENDS in tree:
                dfs(w, idx, c + 1, trie)
            if w[idx] not in tree:
                return
            dfs(w, idx + 1, c, tree[w[idx]])

        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        res = set()
        for w in words:
            if w == "":
                continue
            reduce(dict.__getitem__, w, trie)[self.ENDS] = w
        for w in words:
            dfs(w, 0, 0, trie)
        return list(res)
