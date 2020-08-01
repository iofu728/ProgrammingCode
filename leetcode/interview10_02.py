# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-25 22:13:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-25 22:13:38

"""
面试题 10.02. 变位词组
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

注意：本题相对原题稍作修改

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
通过次数3,405提交次数5,174
"""
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getCounterStr(tokens: str) -> str:
            c = Counter(list(tokens))
            return ",".join(["{}:{}".format(k, c[k]) for k in sorted(c)])

        maps = {}
        for ii in strs:
            cs = getCounterStr(ii)
            if cs not in maps:
                maps[cs] = []
            maps[cs].append(ii)
        return list(maps.values())
