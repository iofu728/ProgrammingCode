# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-24 22:20:07
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-24 22:40:55

"""
小A很喜欢字母N，他认为连续的N串是他的幸运串。有一天小A看到了一个全部由大写字母组成的字符串，他被允许改变最多2个大写字母（也允许不改变或者只改变1个大写字母），使得字符串中所包含的最长的连续的N串的长度最长。你能帮助他吗？
"""
import sys

T = int(sys.stdin.readline().strip())


def get_N(case_id: int):
    S = sys.stdin.readline().strip()
    N = len(S)
    max_len, other_num = 0, 0
    left, right, others = 0, 0, []
    while left <= right and right < N:
        # print(left, right, other_num, others)
        while right < N and other_num <= 2:
            if S[right] != "N":
                other_num += 1
                others.append(right)
            right += 1
        if other_num > 2:
            max_len = max(max_len, right - left - 1)
            left = others[0] + 1
            others = others[1:]
            other_num -= 1
        else:
            max_len = max(max_len, right - left)
    print(max_len)


for case_id in range(T):
    get_N(case_id + 1)
