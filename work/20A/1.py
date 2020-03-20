# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-20 08:59:59
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-20 11:37:01

"""
扑克牌 最小发牌次数
"""

# 1
# 2
# 2 2 2
# 1 1 1 1 1

min_t = 999


def get_2_3(tt):
    ta = [int(ii >= 2) for ii in tt]
    tb = [ii for ii, jj in enumerate(ta) if jj > 0]
    tc = []
    for ii in tb:
        if ii + 1 in tb and ii + 2 in tb:
            tc.append(ii)
    return tc


def get_1_5(tt):
    ta = [int(ii >= 1) for ii in tt]
    tb = [ii for ii, jj in enumerate(ta) if jj > 0]
    tc = []
    for ii in tb:
        if ii + 1 in tb and ii + 2 in tb and ii + 3 in tb and ii + 4 in tb:
            tc.append(ii)
    return tc


def remove(tt, b, length, num):
    return [*tt[:b], *[ii - num for ii in tt[b:b+length]], *tt[b+length:]]


def get_min(tt, t):
    global min_t
    if len([ii for ii in tt if ii < 0]):
        return
    if t > min_t:
        return
    if sum(tt) == 0:
        if t < min_t:
            min_t = t
        return
    # print(tt, t)
    t_1_5 = get_1_5(tt)
    for ii in t_1_5:
        get_min(remove(tt, ii, 5, 1), t + 1)
    t_2_3 = get_2_3(tt)
    for ii in t_2_3:
        get_min(remove(tt, ii, 3, 2), t + 1)
    if len(t_2_3) != 0 or len(t_1_5) != 0:
        return
    for ii, jj in enumerate(tt):
        if jj >= 1:
            get_min(remove(tt, ii, 1, 1), t + 1)
        if jj >= 2:
            get_min(remove(tt, ii, 1, 2), t + 1)
