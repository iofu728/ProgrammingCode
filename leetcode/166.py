# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-03 13:40:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-03 13:41:09

"""
166. Fraction to Recurring Decimal
Medium

1348

2586

Add to List

Share
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
Accepted 164,184 Submissions 715,749
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res, flag = "", numerator * denominator
        num, den = abs(numerator), abs(denominator)
        if not flag:
            return "0"
        if flag < 0:
            res += "-"
        res += str(num // den)
        if num % den == 0:
            return res
        res += "."
        num = num - (num // den) * den
        loop, idx = {}, len(res)
        while num and num not in loop:
            loop[num] = idx
            idx += 1
            num *= 10
            res += str(num // den)
            num = num - (num // den) * den
        if num:
            idx = loop[num]
            res = res[:idx] + "(" + res[idx:] + ")"
        return res
