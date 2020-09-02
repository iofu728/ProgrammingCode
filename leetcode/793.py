# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-01 13:40:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-01 13:41:12

"""
793. Preimage Size of Factorial Zeroes Function Hard
Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many non-negative integers x have the property that f(x) = K.

Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.
Note:

K will be an integer in the range [0, 10^9].
Accepted 8,312 Submissions 20,587
"""

class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def zeta(x):
            return x // 5 + zeta(x // 5) if x > 0 else 0

        left, right = K, 10 * K + 1
        while left < right:
            mid = (left + right) // 2
            mid_v = zeta(mid)
            if mid_v == K:
                return 5
            elif mid_v < K:
                left = mid + 1
            else:
                right = mid
        return 0
