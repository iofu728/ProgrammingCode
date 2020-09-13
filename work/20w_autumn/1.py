# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-13 18:48:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-13 18:57:28


import sys

T = int(sys.stdin.readline().strip())


def get_allocation(case_id: int):
    N, B = [int(ii) for ii in sys.stdin.readline().strip().split()]
    A = [int(ii) for ii in sys.stdin.readline().strip().split() if int(ii) <= B]
    A = sorted(A)
    pay, idx, num = 0, 0, 0
    while idx < len(A):
        if pay + A[idx] <= B:
            pay += A[idx]
            num += 1
            idx += 1
        else:
            break
    print("Case #{}: {}".format(case_id, num))


for case_id in range(T):
    get_allocation(case_id + 1)

