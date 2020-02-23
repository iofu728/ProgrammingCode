# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-02-23 11:47:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-02-23 11:48:38

"""
5172. Largest Multiple of Three
User Accepted:937
User Tried:1529
Total Accepted:989
Total Submissions:3705
Difficulty:Hard
Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

 

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
Example 4:

Input: digits = [0,0,0,0,0,0]
Output: "0"
 

Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
The returning answer must not contain unnecessary leading zeros.
"""


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        out_list = self.get_list(digits)
        if sum(out_list) == 0 and len(out_list) != 0:
            out_list = [0]
        return "".join([str(ii) for ii in out_list])

    def get_list(self, digits: List[int]) -> list:
        list_sum = sum(digits)
        if list_sum == 0:
            return [0]
        digits = sorted(digits, key=lambda i: -i)
        sum_remainder = list_sum % 3
        if sum_remainder == 0:
            return digits
        tt = []
        for ii in range(len(digits) - 1, -1, -1):
            d = digits[ii]
            if d % 3 == sum_remainder:
                return [v for k, v in enumerate(digits) if k != ii]
            elif d % 3 != 0:
                if len(tt) < 2:
                    tt.append((ii, d))
        if len(tt) != 2:
            return []
        return [v for k, v in enumerate(digits) if k != tt[0][0] and k != tt[1][0]]

