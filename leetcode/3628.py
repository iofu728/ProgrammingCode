"""
3628. 插入一个字母的最大子序列数
已解答
中等
premium lock icon
相关企业
提示
给你一个由大写英文字母组成的字符串 s。

你可以在字符串的 任意 位置（包括字符串的开头或结尾）最多插入一个 大写英文字母。

返回在 最多插入一个字母 后，字符串中可以形成的 "LCT" 子序列的 最大 数量。

子序列 是从另一个字符串中删除某些字符（可以不删除）且不改变剩余字符顺序后得到的一个 非空 字符串。

 

示例 1：

输入： s = "LMCT"

输出： 2

解释：

可以在字符串 s 的开头插入一个 "L"，变为 "LLMCT"，其中包含 2 个子序列，分别位于下标 [0, 3, 4] 和 [1, 3, 4]。

示例 2：

输入： s = "LCCT"

输出： 4

解释：

可以在字符串 s 的开头插入一个 "L"，变为 "LLCCT"，其中包含 4 个子序列，分别位于下标 [0, 2, 4]、[0, 3, 4]、[1, 2, 4] 和 [1, 3, 4]。

示例 3：

输入： s = "L"

输出： 0

解释：

插入一个字母无法获得子序列 "LCT"，结果为 0。

 

提示：

1 <= s.length <= 105
s 仅由大写英文字母组成。
"""

class Solution:
    def numOfSubsequences(self, s: str) -> int:
        def get_res(ss):
            res = 0
            L, T = 0, ss[1:].count("T")
            for ii in range(1, n):
                if ss[ii - 1] == "L":
                    L += 1
                if ss[ii] == "T":
                    T -= 1
                if ss[ii] == "C":
                    res += L * T
            return res


        n = len(s)
        res = max(get_res("L" + s), get_res(s + "T"))
        LT = 0
        tmp = get_res(s)
        L, T = 0, s.count("T")
        for ii in range(1, n):
            if s[ii - 1] == "L":
                L += 1
            if s[ii - 1] == "T":
                T -= 1
            LT = max(LT, L * T)
        return max(res, tmp + LT)
        