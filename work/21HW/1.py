# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-01-27 20:35:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-01-27 21:14:35

import collections
import sys

def get_lines():
    A = sys.stdin.readline()
    A = [int(ii) for ii in A.split(",")]
    N, loops = len(A), 0
    a_map = collections.defaultdict(list)
    for ii, jj in enumerate(sorted(A)):
        a_map[jj].append(ii)
    flag = [0] * N
    for ii in range(N):
        if flag[ii] == 0:
            jj = ii
            while (flag[jj] == 0):
                flag[jj] = 1
                jjs = [x for x in a_map[A[jj]] if flag[x] == 0]
                jj1 = [x for x in a_map[A[jj]] if flag[x] == 1]
                if jj1:
                    break
                    jj = jjs[0]
                else:
                    break
            loops += 1
    print(N - loops)

get_lines()

