# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-28 15:51:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-28 15:52:37

"""
1015. Smallest Integer Divisible by K Medium
Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.

Note:

1 <= K <= 10^5
Accepted 11,080 Submissions 34,444
"""


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        def getDiv(num: int):
            have, res = set(), 1
            while num % K:
                if num in have:
                    return -1
                have.add(num)
                num = (num % K) * 10 + 1
                res += 1
            return res

        return getDiv(1)
