# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-18 11:35:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-18 11:49:36

import sys
import bisect
from collections import defaultdict

def get_split():
    n, x, y = [int(ii) for ii in sys.stdin.readline().strip().split()]
    if n <= 0 or n > 2 * y or n < 2 * x:
        return -1
    g = defaultdict(int)
    for ii in sys.stdin.readline().strip().split():
        g[int(ii)] += 1
    gg = []
    for ii in sorted(g.keys()):
        gg.append((gg[-1] if gg else 0) + g[ii])
    l_idx = bisect.bisect_left(gg, x)
    r_idx = bisect.bisect_right(gg, y)
    # print(g, gg, l_idx, r_idx)
    for ii in range(l_idx + 1, r_idx + 1):
        an = n - gg[ii]
        if x <= an <= y:
            return gg[ii]
    return -1

print(get_split())
    

