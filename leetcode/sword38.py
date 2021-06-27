# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-06-22 01:06:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-06-22 01:07:18

"""
剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。


示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8

通过次数105,994提交次数187,397
"""


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = set()

        def dfs(now: str, wait: list):
            if not wait:
                res.add(now)
                return
            for idx, ii in enumerate(wait):
                dfs(now + ii, wait[:idx] + wait[idx + 1 :])

        dfs("", list(s))
        return list(res)