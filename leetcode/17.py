# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-03 21:02:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-03 21:04:00

"""
17. Letter Combinations of a Phone Number Medium
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Accepted 547,581 Submissions 1,210,833
"""


class Solution:
    CHARS = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        N, res = len(digits), []

        def dfs(have: int, tmp: str):
            if have == N:
                if tmp != "":
                    res.append(tmp)
                return
            for ii in self.CHARS[int(digits[have]) - 2]:
                dfs(have + 1, tmp + ii)

        dfs(0, "")
        return res
