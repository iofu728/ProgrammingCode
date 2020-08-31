# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-31 16:24:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-31 16:25:04

"""
1291. Sequential Digits Medium
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
Accepted 12,228 Submissions 22,880
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def gen_seq(begin: int, size: int):
            if begin + size > 10:
                return -1
            res = 0
            for ii in range(size):
                res = res * 10 + (begin + ii)
            return res

        def gen_seqs(size: int):
            tmp = []
            for ii in range(1, 10 - size + 1):
                new = gen_seq(ii, size)
                if new != -1 and low <= new <= high:
                    tmp.append(new)
            return tmp

        B, E = len(str(low)), len(str(high))
        res = []
        for ii in range(B, E + 1):
            res.extend(gen_seqs(ii))
        return res
