# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-18 12:24:14
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-18 12:24:33

"""
100402. 统计满足 K 约束的子字符串数量 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个 二进制 字符串 s 和一个整数 k。

如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：

字符串中 0 的数量最多为 k。
字符串中 1 的数量最多为 k。
返回一个整数，表示 s 的所有满足 k 约束 的子字符串的数量。

 

示例 1：

输入：s = "10101", k = 1

输出：12

解释：

s 的所有子字符串中，除了 "1010"、"10101" 和 "0101" 外，其余子字符串都满足 k 约束。

示例 2：

输入：s = "1010101", k = 2

输出：25

解释：

s 的所有子字符串中，除了长度大于 5 的子字符串外，其余子字符串都满足 k 约束。

示例 3：

输入：s = "11111", k = 1

输出：15

解释：

s 的所有子字符串都满足 k 约束。

 

提示：

1 <= s.length <= 50
1 <= k <= s.length
s[i] 是 '0' 或 '1'。
"""
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        def is_ok(i, j):
            ss = s[i:j]
            return ss.count("0") <= k or ss.count("1") <= k
        res = 0
        N = len(s)
        for i in range(N):
            for j in range(i + 1, N + 1):
                # print(i, j, s[i:j])
                if is_ok(i, j):
                    
                    res += 1
        return res
                