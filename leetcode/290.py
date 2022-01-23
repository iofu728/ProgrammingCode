# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-17 20:28:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-17 20:28:48

"""
290. 单词规律
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

通过次数91,083提交次数200,086
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c = defaultdict(list)
        for ii, jj in enumerate(pattern):
            c[jj].append(ii)
        ss = s.split()
        if len(pattern) != len(ss):
            return False
        for ii, jj in c.items():
            if len(set([ss[kk] for kk in jj])) > 1:
                return False
        if len(set([ss[ii[0]] for ii in c.values()])) != len(c):
            return False
        return True