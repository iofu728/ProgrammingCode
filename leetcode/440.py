# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-03-23 14:34:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-03-23 14:35:43

"""
440. K-th Smallest in Lexicographical Order
Hard

537

73

Add to List

Share
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109
Accepted
17,212
Submissions
56,495
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_num(now):
            x, l, r = 0, now, now
            while l <= n:
                x += min(r, n) - l + 1
                l *= 10
                r = r * 10 + 9
            return x
        cur, k = 1, k - 1
        while k:
            tmp = get_num(cur)
            if tmp <= k:
                k -= tmp
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur
