# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-02 12:03:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-02 12:03:36

"""
100322. 删除星号以后字典序最小的字符串 显示英文描述 
通过的用户数0
尝试过的用户数3
用户总通过次数0
用户总提交次数3
题目难度Medium
给你一个字符串 s 。它可能包含任意数量的 '*' 字符。你的任务是删除所有的 '*' 字符。

当字符串还存在至少一个 '*' 字符时，你可以执行以下操作：

删除最左边的 '*' 字符，同时删除该星号字符左边一个字典序 最小 的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。
请你返回删除所有 '*' 字符以后，剩余字符连接而成的 字典序最小 的字符串。

 

示例 1：

输入：s = "aaba*"

输出："aab"

解释：

删除 '*' 号和它左边的其中一个 'a' 字符。如果我们选择删除 s[3] ，s 字典序最小。

示例 2：

输入：s = "abc"

输出："abc"

解释：

字符串中没有 '*' 字符。

 

提示：

1 <= s.length <= 105
s 只含有小写英文字母和 '*' 字符。
输入保证操作可以删除所有的 '*' 字符。
"""
from sortedcontainers import SortedList
class Solution:
    def clearStars(self, s: str) -> str:
        c = defaultdict(SortedList)
        remove = set()
        star = []
        for ii, jj in enumerate(s):
            if jj == "*":
                star.append(ii)
                continue
            jj = ord(jj) - ord("a")
            c[jj].add(ii)
        # print(c)
        for ii in star:
            for jj in range(26):
                idx = c[jj].bisect(ii)
                if idx == 0:
                    continue
                
                remove.add(c[jj][idx - 1])
                c[jj].remove(c[jj][idx - 1])
                break
        return "".join([jj for ii, jj in enumerate(s) if jj != "*" and ii not in remove])
        
            