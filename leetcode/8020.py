# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-10 13:31:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-10 13:31:38

"""
8020. 字符串转换 显示英文描述 
通过的用户数82
尝试过的用户数254
用户总通过次数89
用户总提交次数572
题目难度Hard
给你两个长度都为 n 的字符串 s 和 t 。你可以对字符串 s 执行以下操作：

将 s 长度为 l （0 < l < n）的 后缀字符串 删除，并将它添加在 s 的开头。
比方说，s = 'abcd' ，那么一次操作中，你可以删除后缀 'cd' ，并将它添加到 s 的开头，得到 s = 'cdab' 。
给你一个整数 k ，请你返回 恰好 k 次操作将 s 变为 t 的方案数。

由于答案可能很大，返回答案对 109 + 7 取余 后的结果。

 

示例 1：

输入：s = "abcd", t = "cdab", k = 2
输出：2
解释：
第一种方案：
第一次操作，选择 index = 3 开始的后缀，得到 s = "dabc" 。
第二次操作，选择 index = 3 开始的后缀，得到 s = "cdab" 。

第二种方案：
第一次操作，选择 index = 1 开始的后缀，得到 s = "bcda" 。
第二次操作，选择 index = 1 开始的后缀，得到 s = "cdab" 。
示例 2：

输入：s = "ababab", t = "ababab", k = 1
输出：2
解释：
第一种方案：
选择 index = 2 开始的后缀，得到 s = "ababab" 。

第二种方案：
选择 index = 4 开始的后缀，得到 s = "ababab" 。
 

提示：

2 <= s.length <= 5 * 105
1 <= k <= 1015
s.length == t.length
s 和 t 都只包含小写英文字母。

"""
mod = 10 ** 9 + 7

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        tmp = t + '#' + s * 2
        n = len(s)
        cnt = 0
        kmp = prep(tmp)
        for i in range(len(kmp)):
            if kmp[i] == n and i - n * 2 < n:
                cnt += 1
        
        grid = [[cnt - 1, cnt], [n - cnt, n - cnt - 1]]
        grid_pow = matrix_pow(grid, k)
        return grid_pow[0][0] if s == t else grid_pow[0][1]

def prep(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j != 0 and p[j] != p[i]:
            j = pi[j - 1]
        if p[j] == p[i]:
            j += 1
        pi[i] = j
    return pi

def matrix_mul(A, B, mod=10 ** 9 + 7):
    n, m = len(A), len(A[0])
    p = len(B[0])
    ans = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                ans[i][k] += A[i][j] * B[j][k]
                ans[i][k] %= mod
    return ans

def matrix_pow(A, n):
    length = len(A)
    tmp = A
    ans = [[0] * length for _ in range(length)]
    for i in range(length):
        ans[i][i] = 1
    for i in range(60):
        if n % 2:
            ans = matrix_mul(ans, tmp)
        tmp = matrix_mul(tmp, tmp)
        n //= 2
    return ans
