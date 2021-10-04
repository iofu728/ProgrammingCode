# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-04 16:48:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-04 16:49:24

"""
241. Different Ways to Add Parentheses
Medium

2768

146

Add to List

Share
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
Accepted
137,913
Submissions
232,141
"""


class Solution:
    OP = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def dfs(s):
            if len(s) == 1:
                return [s[0]]
            return [
                self.OP[s[ii]](a, b)
                for ii in range(1, len(s), 2)
                for a in dfs(s[:ii])
                for b in dfs(s[ii + 1 :])
            ]

        last, idx = 0, 0
        res = []
        while idx < len(expression):
            if expression[idx] in "+-*":
                res.append(int(expression[last:idx]))
                res.append(expression[idx])
                last = idx + 1
            idx += 1
        res.append(int(expression[last:]))
        return dfs(tuple(res))
