# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-09 17:21:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-09 17:23:00

"""
22. Generate Parentheses Medium
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Accepted 493,942 Submissions 816,580
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(now: str, left: int, right: int):
            if left > n or right > n or left < right:
                return
            if left == n and right == n:
                res.append(now)
            dfs(now + "(", left + 1, right)
            dfs(now + ")", left, right + 1)

        dfs("", 0, 0)
        return res
