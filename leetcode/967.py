# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-08 13:24:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-08 13:25:14

"""
967. Numbers With Same Consecutive Differences Medium
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9
Accepted 37,969 Submissions 87,116
"""


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def encoder(s: str):
            if len(s) > 1 and s[0] == "0":
                return
            if len(s) == N:
                res.append(int(s))
                return
            last = int(s[-1])
            if last - K >= 0:
                encoder(s + str(last - K))
            if last + K <= 9 and K:
                encoder(s + str(last + K))

        res = []
        for ii in range(10):
            encoder(str(ii))
        return res
