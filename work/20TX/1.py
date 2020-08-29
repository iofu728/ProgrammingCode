# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-23 19:58:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-26 21:05:39


import sys


def get_a():
    s = sys.stdin.readline().strip()
    N = len(s)
    res = 0
    pos_stack = []
    for ii in s:
        print(ii, res, pos_stack)
        if ii in ["]", ")"]:
            if len(pos_stack):
                last = pos_stack[-1]
                if (last == "[" and ii == "]") or (last == "(" and ii == ")"):
                    pos_stack = pos_stack[:-1]
                else:
                    while len(pos_stack) and (
                        (pos_stack[-1] == "[" and ii == ")")
                        or (pos_stack[-1] == "(" and ii == "]")
                    ):
                        pos_stack = pos_stack[:-1]
                        res += 1
                    if len(pos_stack):
                        pos_stack = pos_stack[:-1]
            else:
                res += 1
        else:
            pos_stack.append(ii)
    res += len(pos_stack)
    print(res)


get_a()


def get_a():
    s = sys.stdin.readline().strip()
    N = len(s)
    res = 0
    pos1, pos2 = 0, 0
    last = 0
    last_map = []
    for ii in s:
        print(pos1, pos2, res, ii, last_map)
        if ii in ["]", ")"]:
            if ii == "]":
                if pos1 == 0:
                    res += 1
                elif last in [1, 0]:
                    pos1 -= 1
                    last_map.pop()
                elif last == 2:
                    res += 1
                    pos1 -= 1
                    pos2 -= 1
                    last_map.pop()
                    last_map.pop()
            else:
                if pos2 == 0:
                    res += 1
                elif last in [2, 0]:
                    pos2 -= 1
                    last_map.pop()
                elif last == 1:
                    res += 1
                    pos1 -= 1
                    pos2 -= 1
                    last_map.pop()
                    last_map.pop()
            if len(last_map) == 0:
                last = 0
            else:
                last = last_map[-1]
        else:
            last_map.append(ii)
            if ii == "[":
                last = 1
                pos1 += 1
            else:
                last = 2
                pos2 += 1
    res += pos1 + pos2
    print(res)


def get_a_v2():
    s = sys.stdin.readline().strip()
    N = len(s)
    dp = [[0] * N for _ in range(N)]
    for ii in range(N - 1):
        if (s[ii] == "(" and s[ii + 1] == ")") or (s[ii] == "[" and s[ii + 1] == "]"):
            dp[ii][ii + 1] = 2
    for ii in range(3, N + 1):
        for jj in range(N - ii - 1):
            kk = jj + ii - 1
            dp[jj][kk] = max(dp[jj][kk], dp[jj + 1][kk + 1])
            dp[jj][kk] = max(dp[jj][kk], max(dp[jj + 1][kk], dp[jj][kk - 1]))
            if (s[jj] == "(" and s[kk] == ")") or (s[jj] == "[" and s[kk] == "]"):
                dp[jj][kk] = max(dp[jj][kk], dp[jj + 1][kk - 1] + 2)
            for p in range(jj + 1, kk):
                dp[jj][kk] = max(dp[jj][kk], dp[jj][p] + dp[p + 1][kk])
    return N - dp[0][N - 1]


print(get_a_v2())
