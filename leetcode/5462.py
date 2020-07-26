# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-26 11:01:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-26 12:32:35

"""
5462. 压缩字符串 II 显示英文描述 
通过的用户数6
尝试过的用户数33
用户总通过次数6
用户总提交次数51
题目难度Hard
行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。

注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。

给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。

请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。

 

示例 1：

输入：s = "aaabcccd", k = 2
输出：4
解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。
示例 2：

输入：s = "aabbaa", k = 2
输出：2
解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。
示例 3：

输入：s = "aaaaaaaaaaa", k = 0
输出：3
解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。
 

提示：

1 <= s.length <= 100
0 <= k <= s.length
s 仅包含小写英文字母
"""


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        dp = [[10 ** 9 + 7] * 111 for _ in range(111)]
        dp[0][0] = 0
        for ii in range(1, N + 1):
            for jj in range(k + 1):
                dp[ii][jj + 1] = min(dp[ii][jj + 1], dp[ii - 1][jj])
                cnt, d = 0, 0
                for l in range(ii, N + 1):
                    cnt += s[l - 1] == s[ii - 1]
                    d += s[l - 1] != s[ii - 1]
                    if jj + d <= k:
                        dp[l][jj + d] = min(
                            dp[l][jj + d],
                            dp[ii - 1][jj]
                            + 1
                            + (
                                3
                                if cnt >= 100
                                else (2 if cnt >= 10 else (1 if cnt >= 2 else 0))
                            ),
                        )
        return dp[N][k]


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        N = len(s)
        change = [ii - 1 for ii in range(1, N) if s[ii - 1] != s[ii]]
        end = change + [N - 1]
        begin = [0] + [ii + 1 for ii in change]
        pairs = [(s[ii], ii, jj) for ii, jj in zip(begin, end)]
        pairMaps = {ii: (jj, jj + 1) for _, ii, jj in pairs}

        def getLen(b, e):
            res, bb = 0, b
            while bb < e:
                ee, nex = pairMaps[bb]
                res += 1 if ee == bb else 2
                bb = nex
            return res

        def getMinSame(pairs, kk):
            res = []
            same = {}
            for a, b, c in pairs:
                if c - b + 1 <= kk:
                    res.append((a, b, c, getLen(b, c)))
                if a not in same:
                    same[a] = []
                same[a].append((b, c))
            for k, v in same.items():
                for idx in range(1, len(v)):
                    ee, bb = v[idx - 1][1], v[idx][0]
                    if bb - ee - 1 <= kk:
                        res.append(
                            (
                                k,
                                ee + 1,
                                bb - 1,
                                bb
                                - ee
                                - 1
                                - getLen(ee + 1, bb - 1)
                                - getLen(bb, v[idx][1]),
                            )
                        )
            if not len(res):
                return res
            print("", res, same)
            return [min(res, key=lambda i: i[-1])]

        while k:
            remove = getMinSame(pairs, k)
            if remove == []:
                minLen = min(
                    pairs,
                    key=lambda i: i[-1] - i[1]
                    if (i[-1] - i[1] + 1) // 10 == 0
                    else (i[-1] - i[1] + 1 - 9) % 10,
                )
                pairs = [(a, b, (c - k if b == minLen[1] else c)) for a, b, c in pairs]
                break
            remove = remove[0]
            k -= remove[2] - remove[1] + 1
            print(remove)
            pairs = [
                (a, b, c)
                for a, b, c in pairs
                if not (b >= remove[1] and c <= remove[2])
            ]
            if len(pairs):
                now = [pairs[0]]
                for a, b, c in pairs[1:]:
                    if a == now[-1][0]:
                        now[-1] = (a, now[-1][1], c)
                    else:
                        now.append((a, b, c))
                pairs = now
                pairMaps = {}
                for ii in range(len(pairs) - 1):
                    a, b, c = pairs[ii]
                    pairMaps[b] = (c, pairs[ii + 1][1])
                _, b, c = pairs[-1]
                pairMaps[b] = (c, N)
                print(pairs, pairMaps)
        print(pairs)
        return sum(
            [1 if (e - b + 1) == 1 else len(str(e - b + 1)) + 1 for _, b, e in pairs]
        )

