"""
567. 字符串的排列
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

 

示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false
 

提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母
通过次数152,063提交次数348,713
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        N, M = len(s1), len(s2)
        if N > M:
            return False

        c2 = Counter(s2[:N])
        if c1 == c2:
            return True
        for ii in range(N, M):
            c2[s2[ii - N]] -= 1
            c2[s2[ii]] += 1
            if c1 == c2:
                return True
        return False
