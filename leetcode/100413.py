# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-09-15 12:43:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-09-15 12:43:47

"""
100413. 形成目标字符串需要的最少字符串数 II 显示英文描述 
通过的用户数0
尝试过的用户数3
用户总通过次数0
用户总提交次数4
题目难度Hard
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
1 <= words[i].length <= 5 * 104
输入确保 sum(words[i].length) <= 105.
words[i]  只包含小写英文字母。
1 <= target.length <= 5 * 104
target  只包含小写英文字母。
"""
def z_algorithm(s: string):
    s = [ord(c) for c in s]
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if j + z[j] < i + z[i]:
            j = i
    z[0] = n
    return z


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        ls = [0]*n
        for w in words:
            s = w+"#"+target
            ps = z_algorithm(s)
            for i in range(len(w)+1, len(s)):
                ls[i-len(w)-1] = max(ls[i-len(w)-1], ps[i])

        n = len(target)
        dp = [-1]*(n+1)
        dp[0] = 0
        last = 0
        for i in range(n):
            if dp[i] == -1:
                continue
            if i > last:
                return -1
            mx = ls[i]
            if i+mx > last:
                for j in range(last+1, i+mx+1):
                    dp[j] = dp[i]+1
                last = i+mx
            if last == n:
                break
        return dp[n]