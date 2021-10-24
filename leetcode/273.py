# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-10-11 00:34:46
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-10-11 00:35:12

"""
273. Integer to English Words
Hard

1728

4216

Add to List

Share
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 231 - 1
Accepted
263,827
Submissions
910,613
"""

singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = [
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
]
tens = [
    "",
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
]
thousands = ["", "Thousand", "Million", "Billion"]


class Solution:
    def numberToWords(self, num: int) -> str:
        def toe(num):
            res = ""
            if num >= 100:
                res += singles[num // 100] + " Hundred "
                num %= 100
            if num >= 20:
                res += tens[num // 10] + " "
                num %= 10
            if 0 < num < 10:
                res += singles[num] + " "
            elif num >= 10:
                res += teens[num - 10] + " "
            return res

        if num == 0:
            return "Zero"
        res, unit = "", 10 ** 9
        for ii in range(3, -1, -1):
            tmp = num // unit
            if tmp:
                num -= tmp * unit
                res += toe(tmp) + thousands[ii] + " "
            unit //= 1000
        return res.strip()
