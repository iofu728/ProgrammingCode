# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-12 10:30:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-12 10:32:58

"""
5380. String Matching in an Array
User Accepted:123
User Tried:192
Total Accepted:123
Total Submissions:215
Difficulty:Easy
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.
"""


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=lambda i: len(i))
        tt = "||".join(words)
        res = []
        for ii in words:
            if tt.count(ii) >= 2:
                res.append(ii)
        return res
