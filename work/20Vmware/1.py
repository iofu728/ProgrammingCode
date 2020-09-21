# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-21 20:46:13
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-21 21:23:06

import sys

n, m, r = [float(ii) for ii in sys.stdin.readline().strip().split()]
m = int(m)


def get_point():
    def get_id(begin, end, dirs=1):
        nonlocal tt
        tmp = []
        ii = begin
        while ii < end if dirs > 0 else ii > end:
            if tt <= 0:
                return tmp
            tmp.append(ii)
            tt -= 1
            ii += r * dirs
        return tmp

    res, t, tt = [], 0, m
    while tt > 0:
        ta = get_id(r - (4 * t * n) % r, n)
        res.extend([(ii, 0) for ii in ta])
        ta = get_id((r - (1 + 4 * t) * n) % r, n)
        res.extend([(n, ii) for ii in ta])
        ta = get_id(n - (r - ((2 + 4 * t) * n) % r), -1, -1)
        res.extend([(ii, n) for ii in ta])
        ta = get_id(n - (r - ((3 + 4 * t) * n) % r), -1, -1)
        res.extend([(0, ii) for ii in ta])
        t += 1

    for ii, jj in res:
        print("{:.2f} {:.2f}".format(ii, jj))


get_point()
