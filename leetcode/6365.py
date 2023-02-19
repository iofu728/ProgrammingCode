# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-02-19 12:54:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-02-19 12:54:41


class Solution:
    def minOperations(self, n: int) -> int:
        s = bin(n)[2:]
        res = bin(n)[2:].count("1")
        # idx = 0
        idx = len(s) - 1
        n = 0

        while idx >= 0 and s[idx] == "0":
            idx -= 1
        while idx >= 0:
            n = 0
            while idx >= 0 and s[idx] == "1":
                n += 1
                idx -= 1
            # print("m", n, idx)
            while n > 0 and idx > 0 and s[idx] == "0" and s[idx - 1] == "1":
                # print("x", idx, n)
                idx -= 1
                n -= 1
                while idx >= 0 and s[idx] == "1":
                    n += 1
                    idx -= 1
            idx -= 1
            # print(idx, n)
            if n > 2:
                res -= n - 2
        return res


#         if res == len(s):
#             res = min(res, 1)

#         for ii in range(len(s) - 1, -1)
#         return .count("1")

from functools import lru_cache


def lowbit(n):
    return n & (-n)


@lru_cache(None)
def f(n):
    if (n & (n - 1)) == 0:
        return 1
    lb = lowbit(n)
    return min(f(n - lb), f(n + lb)) + 1


class Solution:
    def minOperations(self, n: int) -> int:
        return f(n)
