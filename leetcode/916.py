# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-27 18:56:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-27 18:57:22

"""
916. Word Subsets Medium
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
 

Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
Accepted 21,520 Submissions 45,034
"""
from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def in_it(a: dict, b: dict):
            for k, v in a.items():
                if k not in b or b[k] < v:
                    return False
            return True

        need = {}
        for ii in B:
            tmp = Counter(ii)
            for k, v in tmp.items():
                need[k] = max(v, need.get(k, 0))
        res = []
        for ii in A:
            have = Counter(ii)
            if in_it(need, have):
                res.append(ii)
        return res
