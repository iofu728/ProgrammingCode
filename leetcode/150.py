# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-01 12:03:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-01 12:04:12

"""
150. Evaluate Reverse Polish Notation Medium
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
Accepted 244,127 Submissions 663,437
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def cal(a, b, c):
            if c == "+":
                return a + b
            if c == "-":
                return a - b
            if c == "*":
                return a * b
            return int(a / b)

        stack, idx, N = [], 0, len(tokens)
        while idx < N:
            if tokens[idx] in "+-*/":
                a = stack.pop()
                b = stack.pop()
                stack.append(cal(b, a, tokens[idx]))
            else:
                stack.append(int(tokens[idx]))
            # print(idx, stack)
            idx += 1
        return stack[0]
