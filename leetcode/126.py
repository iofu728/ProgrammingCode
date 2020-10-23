# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-23 22:52:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-23 22:53:10

"""
126. Word Ladder II Hard
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
Accepted 201,099 Submissions 882,347
"""
from collections import defaultdict
import heapq


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        def get_edge(s: str):
            for ii in range(len(s)):
                for jj in g[s[:ii] + "*" + s[ii + 1 :]]:
                    if jj not in flags:
                        yield jj

        N, g = len(wordList), defaultdict(list)
        for ii in wordList:
            for jj in range(len(ii)):
                g[ii[:jj] + "*" + ii[jj + 1 :]].append(ii)

        res, min_v = [], None
        flags = set()
        queue, idx = [(0, 0, beginWord, [beginWord])], 1
        while queue:
            h, _, w, pre = heapq.heappop(queue)
            flags.add(w)
            if w == endWord:
                if min_v is None:
                    min_v = h
                    res.append(pre)
                elif min_v == h:
                    res.append(pre)
                continue
            for ii in get_edge(w):
                if ii not in flags:
                    heapq.heappush(queue, (h + 1, idx, ii, pre + [ii]))
                    idx += 1
        return res
