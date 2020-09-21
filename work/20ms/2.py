# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-21 19:22:23
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-21 19:47:17


def test(input1, input2):
    tt = input1.split()
    res = 0
    for ii in tt:
        size = input2 % len(ii)
        if not size:
            res += 1
        elif ii[-size:] + ii[:-size] == ii:
            res += 1
    return res
