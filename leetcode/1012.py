# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-26 23:15:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-26 23:16:02

"""
1012. Numbers With Repeated Digits Hard
Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.

Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262

Note:

1 <= N <= 10^9
Accepted 5,262 Submissions 14,077
"""
from collections import Counter


class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def is_ok(num: int):
            c = Counter(str(num))
            for k, v in c.items():
                if v > 1:
                    return False
            return True

        def get_C(num: int, c: int = 9):
            A = 1
            for ii in range(num):
                A *= c - ii
            # for jj in range(1, num):
            #     A /= (jj + 1)
            return int(A)

        NN = str(N)
        size = len(NN)
        res = sum([get_C(1) * get_C(ii - 1) for ii in range(1, size)])
        print(res)
        for ii in range(size):
            ago = NN[:ii]
            if ago and not is_ok(int(ago)):
                break
            tmp = len(
                [
                    jj
                    for jj in range(int(NN[ii]))
                    if (str(jj) not in ago and jj != 0)
                    or (jj == 0 and ii != 0 and str(jj) not in ago)
                ]
            )
            # if ii == 0:
            #     tmp -= 1
            b = get_C(size - ii - 1, 9 - ii)
            print(tmp, b, ii)
            tmp *= b
            res += tmp

        if is_ok(N):
            res += 1

        return N - res
