# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-04-01 10:57:00
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-04-01 11:02:58

"""
479. Largest Palindrome Product
Hard

122

1441

Add to List

Share
Given an integer n, return the largest palindromic integer that can be represented as the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.

 

Example 1:

Input: n = 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
Example 2:

Input: n = 1
Output: 9
 

Constraints:

1 <= n <= 8
Accepted
19,959
Submissions
64,632
"""
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        for ii in range(10 ** n - 1, -1, -1):
            px = int(str(ii) + str(ii)[::-1])
            for jj in range(10 ** n - 1, isqrt(px), -1):
                if px % jj == 0:
                    return px % 1337
