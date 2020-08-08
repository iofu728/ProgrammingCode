# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-08 15:55:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-08 16:06:48

import sys

D = [int(ii) for ii in sys.stdin.readline().strip().split()]


def get_score():
    score = sum([ii * jj for ii, jj in zip(range(1, 6), D)])
    num = sum(D)
    if num == 0:
        return 0
    return score / num


print("{:f}".format(get_score())[:3])
