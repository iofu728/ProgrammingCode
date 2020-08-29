# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-23 20:32:10
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-23 20:37:30


import sys

T = int(sys.stdin.readline().strip())


def get_area(case_id: int):
    A, B, C, D = [int(ii) for ii in sys.stdin.readline().strip().split()]
    a = A * (D ** 3) / 3 + (D ** 2) / 2 + B * D
    b = A * (C ** 3) / 3 + (C ** 2) / 2 + B * C
    print("{:.6f}".format(a - b))


for case_id in range(T):
    get_area(case_id + 1)

