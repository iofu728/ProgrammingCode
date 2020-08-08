# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-08 20:42:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-08 20:55:50

import sys

A = sys.stdin.readline().strip()


def getMaxLower(number: str):
    N = len(number)
    for ii in range(1, N + 1):
        last = number[-ii:]
        tmp = "".join(sorted(last))
        if last == tmp or (ii == N and tmp[0] == "0"):
            continue
        first_idx = max([jj for jj, ii in enumerate(last) if ii < last[0]])
        other = last[:first_idx] + tmp[first_idx + 1 :]
        other = "".join(sorted(other, reverse=True))

        return number[:-ii] + last[first_idx] + other
    return 0


print(getMaxLower(A))
