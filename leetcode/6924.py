# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-07-16 11:42:24
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-07-16 11:42:35

"""
6924. 最长合法子字符串的长度 显示英文描述 
通过的用户数55
尝试过的用户数92
用户总通过次数59
用户总提交次数152
题目难度Hard
给你一个字符串 word 和一个字符串数组 forbidden 。

如果一个字符串不包含 forbidden 中的任何字符串，我们称这个字符串是 合法 的。

请你返回字符串 word 的一个 最长合法子字符串 的长度。

子字符串 指的是一个字符串中一段连续的字符，它可以为空。

 

示例 1：

输入：word = "cbaaaabc", forbidden = ["aaa","cb"]
输出：4
解释：总共有 9 个合法子字符串："c" ，"b" ，"a" ，"ba" ，"aa" ，"bc" ，"baa" ，"aab" 和 "aabc" 。最长合法子字符串的长度为 4 。
其他子字符串都要么包含 "aaa" ，要么包含 "cb" 。
示例 2：

输入：word = "leetcode", forbidden = ["de","le","e"]
输出：4
解释：总共有 11 个合法子字符串："l" ，"t" ，"c" ，"o" ，"d" ，"tc" ，"co" ，"od" ，"tco" ，"cod" 和 "tcod" 。最长合法子字符串的长度为 4 。
所有其他子字符串都至少包含 "de" ，"le" 和 "e" 之一。
 

提示：

1 <= word.length <= 105
word 只包含小写英文字母。
1 <= forbidden.length <= 105
1 <= forbidden[i].length <= 10
forbidden[i] 只包含小写英文字母。
"""

class Solution:
    ENDS = "#"
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        N = len(word)
        
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        res = set()
        for w in forbidden:
            if w == "":
                continue
            reduce(dict.__getitem__, w, trie)[self.ENDS] = w
        l, r, res = 0, 0, 0
        while l < N and r < N:
            flag = True
            q = [trie]
            while r < N:
                tmp = [trie]
                for x in q:
                    if word[r] in x:
                        new_trie = x[word[r]]
                        if self.ENDS in new_trie:
                            res = max(res, r - l)
                            l = r - len(new_trie[self.ENDS]) + 2
                            r = l
                            flag = False
                            # print(l, r)
                            break
                        tmp.append(new_trie)
                if not flag:
                    break
                q = tmp
                r += 1
                # print(r)
            if flag:
                res = max(res, r - l)
        return res
            