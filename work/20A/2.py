# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-03-20 11:40:29
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-03-20 12:16:34

"""
N = 4
tt = ["aaa", "bcd", "zzz", "bcdef"]
"""

# char = [chr(i) for i in range(97, 123)]


def max_length(N: int, tt: list):
    dp = {ii: 0 for ii in range(26)}
    ta = [(ord(ii[0]) - ord("a"), ord(ii[-1]) - ord("a"), len(ii))
          for ii in tt]
    ta = sorted(ta)
    for b, e, l in ta:
        ago = [dp[ii] for ii in range(b)]
        temp_max = max(ago) if len(ago) else 0
        # print(temp_max, l)
        dp[e] = max(dp[e], temp_max + l)
    return max(dp.values())
    # return dp[25]
