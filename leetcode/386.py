# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-15 12:37:08
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-15 12:41:47

"""
386. Lexicographical Numbers Medium
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

Accepted 56,300 Submissions 108,107
"""


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur: int):
            if cur > n:
                return
            if cur:
                res.append(cur)
            for ii in range(10):
                if cur * 10 + ii > n:
                    return
                dfs(cur * 10 + ii)

        res = []
        for ii in range(1, 10):
            dfs(ii)
        return res
