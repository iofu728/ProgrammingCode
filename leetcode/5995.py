# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-30 13:39:05
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-30 13:39:19

"""
5995. 字符串分组 显示英文描述 
通过的用户数104
尝试过的用户数291
用户总通过次数111
用户总提交次数794
题目难度Hard
给你一个下标从 0 开始的字符串数组 words 。每个字符串都只包含 小写英文字母 。words 中任意一个子串中，每个字母都至多只出现一次。

如果通过以下操作之一，我们可以从 s1 的字母集合得到 s2 的字母集合，那么我们称这两个字符串为 关联的 ：

往 s1 的字母集合中添加一个字母。
从 s1 的字母集合中删去一个字母。
将 s1 中的一个字母替换成另外任意一个字母（也可以替换为这个字母本身）。
数组 words 可以分为一个或者多个无交集的 组 。一个字符串与一个组如果满足以下 任一 条件，它就属于这个组：

它与组内 至少 一个其他字符串关联。
它是这个组中 唯一 的字符串。
注意，你需要确保分好组后，一个组内的任一字符串与其他组的字符串都不关联。可以证明在这个条件下，分组方案是唯一的。

请你返回一个长度为 2 的数组 ans ：

ans[0] 是 words 分组后的 总组数 。
ans[1] 是字符串数目最多的组所包含的字符串数目。
 

示例 1：

输入：words = ["a","b","ab","cde"]
输出：[2,3]
解释：
- words[0] 可以得到 words[1] （将 'a' 替换为 'b'）和 words[2] （添加 'b'）。所以 words[0] 与 words[1] 和 words[2] 关联。
- words[1] 可以得到 words[0] （将 'b' 替换为 'a'）和 words[2] （添加 'a'）。所以 words[1] 与 words[0] 和 words[2] 关联。
- words[2] 可以得到 words[0] （删去 'b'）和 words[1] （删去 'a'）。所以 words[2] 与 words[0] 和 words[1] 关联。
- words[3] 与 words 中其他字符串都不关联。
所以，words 可以分成 2 个组 ["a","b","ab"] 和 ["cde"] 。最大的组大小为 3 。
示例 2：

输入：words = ["a","ab","abc"]
输出：[1,3]
解释：
- words[0] 与 words[1] 关联。
- words[1] 与 words[0] 和 words[2] 关联。
- words[2] 与 words[1] 关联。
由于所有字符串与其他字符串都关联，所以它们全部在同一个组内。
所以最大的组大小为 3 。
 

提示：

1 <= words.length <= 2 * 104
1 <= words[i].length <= 26
words[i] 只包含小写英文字母。
words[i] 中每个字母最多只出现一次。
"""
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        def find_father(idx):
            while not idx == fa[idx]:
                fa[idx] = fa[fa[idx]]
                idx = fa[idx]
            return idx
        def union(a, b):
            ax, bx = find_father(a), find_father(b)
            fa[ax] = bx

        nwords = []
        for w in words:
            t = 0
            for ii in w:
                t |= (1 << (ord(ii) - ord("a")))
            nwords.append(t)
        c = Counter(nwords)
        words = list(c.keys())
        N = len(words)
        fa = {ii: ii for ii in words}
        nums = {ii: 0 for ii in words}
        for w in words:
            for ii in range(26):
                if w & (1 << ii) == 0:
                    continue
                tmp = w - (1 << ii)
                if tmp in fa:
                    union(w, tmp)
                for jj in range(26):
                    if w & (1 << jj) > 0:
                        continue
                    t = tmp + (1 << jj)
                    if t in fa:
                        union(w, t)
            for jj in range(26):
                if w & (1 << jj) > 0:
                    continue
                t = w + (1 << jj)
                if t in fa:
                    union(w, t)
        res = set()
        for ii in words:
            x = find_father(ii)
            res.add(x)
            nums[x] += c[ii]
        return [len(res), max(nums.values())]
