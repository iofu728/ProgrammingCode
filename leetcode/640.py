# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-07 21:54:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-07 21:59:18

"""
640. Solve the Equation Medium
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
Accepted 25,481 Submissions 60,412
"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        def split(s: str):
            res = []
            pre = ""
            for ii in s:
                if ii in ["+", "-"]:
                    if pre != "":
                        res.append(pre)
                    pre = "" if ii != "-" else "-"
                else:
                    pre += ii
            if pre != "":
                res.append(pre)
            return res

        def decoder(s: list):
            return [
                (
                    int(
                        ii.replace("x", "")
                        if ii not in ["x", "-x"]
                        else ii.replace("x", "1")
                    ),
                    int("x" in ii),
                )
                for ii in s
            ]

        a, b = equation.split("=")
        aa, bb = split(a), split(b)
        # print(aa, bb)
        aa, bb = decoder(aa), decoder(bb)
        # print(aa, bb)
        x_num, const_num = 0, 0
        for num_list, t in [(aa, 1), (bb, -1)]:
            for ii, jj in num_list:
                if jj == 1:
                    x_num += ii * t
                else:
                    const_num += ii * t
        # print(x_num, const_num)
        if x_num == 0:
            if const_num == 0:
                return "Infinite solutions"
            return "No solution"
        return "x={}".format(-const_num // x_num)
