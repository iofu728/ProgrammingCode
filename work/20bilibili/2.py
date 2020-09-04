# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-04 19:45:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-04 20:19:00

import sys

T = sys.stdin.readline().strip()


def get_arr(arr: str):
    if not len(arr):
        return 0
    arr = arr.replace(" ", "")
    arr = [int(ii) for ii in arr.split(",")]
    for ii in range(1, len(arr)):
        arr[ii] += max(arr[ii - 1], 0)
    if len(arr):
        return max(arr)
    return 0


print(get_arr(T))

