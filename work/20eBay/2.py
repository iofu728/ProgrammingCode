# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-16 19:43:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-16 19:58:56

import sys

T = int(sys.stdin.readline())


def get_correct():
    s = sys.stdin.readline().strip()
    if len(s) >> 1 << 1 != len(s):
        return False
    A = []
    for ii in s:
        if ii in "{[(":
            A.append(ii)
        else:
            t = A.pop()
            need = "(" if ii == ")" else ("[" if ii == "]" else "{")
            if t != need:
                return False
    return True


for ii in range(T):
    print("Yes" if get_correct() else "No")
