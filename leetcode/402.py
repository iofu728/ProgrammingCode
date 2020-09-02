# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-01 15:20:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-01 15:24:55

"""
402. Remove K Digits Medium
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
Accepted 151,848 Submissions 534,346
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def dp(s: str, n: int):
            if n <= 1:
                return ""
            idx, pre = 0, int(s[0]) 
            while idx + 1 < n and int(s[idx + 1]) >= pre:
                pre = int(s[idx + 1])
                idx += 1
            # print(idx)
            if idx == n:
                return s[1:]
            return s[:idx] + s[idx + 1:]
        N = len(num)
        res, n = num, N
        for ii in range(k):
            res = dp(res, n)
            n -= 1
        idx = 0
        while idx < n and res[idx] == "0":
            idx += 1
        if idx == n:
            return "0"
        return res[idx:]