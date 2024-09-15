# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-09-15 12:44:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-09-15 12:44:16

"""
100415. 形成目标字符串需要的最少字符串数 I 显示英文描述 
通过的用户数3
尝试过的用户数7
用户总通过次数3
用户总提交次数8
题目难度Medium
给你一个字符串数组 words 和一个字符串 target。

如果字符串 x 是 words 中 任意 字符串的 前缀，则认为 x 是一个 有效 字符串。

现计划通过 连接 有效字符串形成 target ，请你计算并返回需要连接的 最少 字符串数量。如果无法通过这种方式形成 target，则返回 -1。

 

示例 1：

输入： words = ["abc","aaaaa","bcdef"], target = "aabcdabc"

输出： 3

解释：

target 字符串可以通过连接以下有效字符串形成：

words[1] 的长度为 2 的前缀，即 "aa"。
words[2] 的长度为 3 的前缀，即 "bcd"。
words[0] 的长度为 3 的前缀，即 "abc"。
示例 2：

输入： words = ["abababab","ab"], target = "ababaababa"

输出： 2

解释：

target 字符串可以通过连接以下有效字符串形成：

words[0] 的长度为 5 的前缀，即 "ababa"。
words[0] 的长度为 5 的前缀，即 "ababa"。
示例 3：

输入： words = ["abcdef"], target = "xyz"

输出： -1

 

提示：

1 <= words.length <= 100
1 <= words[i].length <= 5 * 103
输入确保 sum(words[i].length) <= 105。
words[i] 只包含小写英文字母。
1 <= target.length <= 5 * 103
target 只包含小写英文字母。
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False  # Not needed in this problem as any node represents a valid prefix

class Solution:
    def minValidStrings(self, words, target):
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Build the trie
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

        # DP to find the minimal number of substrings
        for i in range(n):
            if dp[i] != float('inf'):
                node = root
                for j in range(i, n):
                    c = target[j]
                    if c in node.children:
                        node = node.children[c]
                        dp[j + 1] = min(dp[j + 1], dp[i] + 1)
                    else:
                        break

        return -1 if dp[n] == float('inf') else dp[n]
