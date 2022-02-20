# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-02-20 11:32:48
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-02-20 11:33:14

"""
6014. 构造限制重复的字符串 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。

返回 字典序最大的 repeatLimitedString 。

如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。

 

示例 1：

输入：s = "cczazcc", repeatLimit = 3
输出："zzcccac"
解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
字母 'a' 连续出现至多 1 次。
字母 'c' 连续出现至多 3 次。
字母 'z' 连续出现至多 2 次。
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。
示例 2：

输入：s = "aababab", repeatLimit = 2
输出："bbabaa"
解释：
使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 
字母 'a' 连续出现至多 2 次。 
字母 'b' 连续出现至多 2 次。 
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 
该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 
注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。
 

提示：

1 <= repeatLimit <= s.length <= 105
s 由小写英文字母组成
"""


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = Counter(s)
        keys = sorted(c.keys(), reverse=True)
        res = ""
        idx = 0
        # q = [for ii in ]
        while idx < len(keys):
            ii = keys[idx]
            jj = c[keys[idx]]
            while jj > repeatLimit:
                if idx >= len(keys) - 1:
                    break
                # print(idx)
                idx += 1
                k, kk = keys[idx], c[keys[idx]]
                need = (jj - 1) // repeatLimit
                have = min(need, kk)

                res += (ii * repeatLimit + k) * have
                jj -= repeatLimit * have
                # print(have, jj)
                if kk - have:
                    c[k] -= have
                    idx -= 1
                    break

            if jj > 0:
                res += ii * min(jj, repeatLimit)
            idx += 1
            # print(idx,ii, jj )

        return res
