# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-08 19:50:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-08 20:41:22

import sys
import re

A = sys.stdin.readline().strip()


def getCameCase(a):
    a = re.findall("[0-9a-zA-Z]+", a)
    res = ""
    for ii in a:
        if ii == "":
            continue
        if res != "":
            res += ii.capitalize()
        else:
            res += ii.lower()
    return res


print(getCameCase(A))
