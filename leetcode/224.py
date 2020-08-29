# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-28 17:57:06
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-28 17:58:48

"""
224. Basic Calculator Hard
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
Accepted 167,870 Submissions 454,103
"""


class Solution:
    def calculate(self, s: str) -> int:
        def decoder(stack: list):
            res = stack.pop() if stack else 0
            while stack and stack[-1] != ")":
                sign = stack.pop()
                if sign == "+":
                    res += stack.pop()
                else:
                    res -= stack.pop()
            return res

        s = s.replace(" ", "")
        stack = []
        N, n, op = len(s), 0, 0
        for ii in range(N - 1, -1, -1):
            now = s[ii]
            if now.isdigit():
                op = 10 ** n * int(now) + op
                n += 1
            else:
                if n:
                    stack.append(op)
                    n, op = 0, 0
                if now == "(":
                    res = decoder(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(now)
        if n:
            stack.append(op)
        return decoder(stack)

