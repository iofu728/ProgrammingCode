"""
100245. 每个字符最多出现两次的最长子字符串 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度。

 

示例 1：

输入： s = "bcbbbcba"

输出： 4

解释：

以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。

示例 2：

输入： s = "aaaa"

输出： 2

解释：

以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。

 

提示：

2 <= s.length <= 100
s 仅由小写英文字母组成。
"""
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        N = len(s)
        res = 2
        for ii in range(N):
            c = defaultdict(int)
            c[s[ii]] += 1
            flag = True
            for jj in range(ii + 1, N):
                c[s[jj]] += 1
                if c[s[jj]] > 2:
                    # print(ii, jj)
                    res = max(res, jj - ii)
                    flag = False
                    break
            if flag:
                res = max(res, N - ii)
        return res