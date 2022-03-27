# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-25 11:03:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-25 11:04:40

"""
172. Factorial Trailing Zeroes
Medium

1912

1651

Add to List

Share
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
 

Follow up: Could you write a solution that works in logarithmic time complexity?

Accepted
310,561
Submissions
764,528
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        def get_k(k):
            res = 0
            ii, ii_n = k, 1
            while ii <= n:
                res += (n // ii) * ii_n
                ii *= k
                # ii_n += 1
            return res
        
        five, two = get_k(5), get_k(2)
        # print(five, two)
        return min(five, two)
