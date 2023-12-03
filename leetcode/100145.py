# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-12-03 12:02:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-12-03 12:02:20

"""
100145. 统计完全子字符串 显示英文描述 
通过的用户数38
尝试过的用户数224
用户总通过次数38
用户总提交次数453
题目难度Medium
给你一个字符串 word 和一个整数 k 。

如果 word 的一个子字符串 s 满足以下条件，我们称它是 完全字符串：

s 中每个字符 恰好 出现 k 次。
相邻字符在字母表中的顺序 至多 相差 2 。也就是说，s 中两个相邻字符 c1 和 c2 ，它们在字母表中的位置相差 至多 为 2 。
请你返回 word 中 完全 子字符串的数目。

子字符串 指的是一个字符串中一段连续 非空 的字符序列。

 

示例 1：

输入：word = "igigee", k = 2
输出：3
解释：完全子字符串需要满足每个字符恰好出现 2 次，且相邻字符相差至多为 2 ：igigee, igigee, igigee 。
示例 2：

输入：word = "aaabbbccc", k = 3
输出：6
解释：完全子字符串需要满足每个字符恰好出现 3 次，且相邻字符相差至多为 2 ：aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc 。
 

提示：

1 <= word.length <= 105
word 只包含小写英文字母。
1 <= k <= word.length

"""
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        j = 0
        ans = 0
        s = [0] * n
        pos = [[] for _ in range(26)]
        for i in range(n):
            c = ord(word[i]) - ord("a")
            if i and abs(ord(word[i]) - ord(word[i - 1])) > 2:
                j = i
            for x in range(pos[c][-1] + 1 if len(pos[c]) else 0, i + 1):
                s[x] += 1
            pos[c].append(i)
            if len(pos[c]) > k:
                j = max(j, pos[c][-k - 1] + 1)
            for x in range(1, 27):
                if x * k > i - j + 1:
                    break
                ans += s[i - x * k + 1] == x
        return ans