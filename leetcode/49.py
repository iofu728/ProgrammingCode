# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-06 14:25:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-06 14:25:46

"""
49. Group Anagrams Medium
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
Accepted 736,156 Submissions 1,285,138
"""
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encoder(s: str):
            c = Counter(s)
            res = ""
            for k in sorted(c):
                res += "{}{}".format(k, c[k] if c[k] > 1 else "")
            return res

        res = defaultdict(list)
        for s in strs:
            encoder_s = encoder(s)
            res[encoder_s].append(s)
        return list(res.values())
