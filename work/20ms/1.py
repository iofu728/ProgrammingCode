# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-21 19:00:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-21 22:50:36


def test(input1, input2):
    def check(tgt, left, right):
        t, pre = 0, 0
        while left <= right:
            if t > 1:
                break
            if left == right or tgt != input2[left] + input2[right]:
                t += 1
                pre = input2[left]
            left += 1
            right -= 1
        return t, pre

    if input1 == 3:
        return input2[0] + input2[1] - input2[0]
    a, b, c = input2[0] + input2[-1], input2[0] + input2[-2], input2[1] + input2[-1]
    for tgt, left, right, o in [
        (a, 0, input1 - 1, 0),
        (b, 0, input1 - 2, input2[-1]),
        (c, 1, input1 - 1, input2[0]),
    ]:
        t, pre = check(tgt, left, right)
        if t > 1:
            continue
        if t == 1:
            if tgt - pre == pre:
                continue
            return tgt - pre
        if t == 0:
            return tgt - o


def test():
    