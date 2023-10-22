# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-10-12 22:55:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-10-12 22:55:25

"""
2896. 执行操作使两个字符串相等 显示英文描述 
通过的用户数339
尝试过的用户数1306
用户总通过次数394
用户总提交次数4236
题目难度Medium
给你两个下标从 0 开始的二进制字符串 s1 和 s2 ，两个字符串的长度都是 n ，再给你一个正整数 x 。

你可以对字符串 s1 执行以下操作 任意次 ：

选择两个下标 i 和 j ，将 s1[i] 和 s1[j] 都反转，操作的代价为 x 。
选择满足 i < n - 1 的下标 i ，反转 s1[i] 和 s1[i + 1] ，操作的代价为 1 。
请你返回使字符串 s1 和 s2 相等的 最小 操作代价之和，如果无法让二者相等，返回 -1 。

注意 ，反转字符的意思是将 0 变成 1 ，或者 1 变成 0 。

 

示例 1：

输入：s1 = "1100011000", s2 = "0101001010", x = 2
输出：4
解释：我们可以执行以下操作：
- 选择 i = 3 执行第二个操作。结果字符串是 s1 = "1101111000" 。
- 选择 i = 4 执行第二个操作。结果字符串是 s1 = "1101001000" 。
- 选择 i = 0 和 j = 8 ，执行第一个操作。结果字符串是 s1 = "0101001010" = s2 。
总代价是 1 + 1 + 2 = 4 。这是最小代价和。
示例 2：

输入：s1 = "10110", s2 = "00011", x = 4
输出：-1
解释：无法使两个字符串相等。
 

提示：

n == s1.length == s2.length
1 <= n, x <= 500
s1 和 s2 只包含字符 '0' 和 '1' 。

"""

class Solution:
    def minOperations(self, s1: str, s2: str, z: int) -> int:
        @lru_cache(None)
        def dfs(idx, a):
            # a, b = 0, 0
            if idx < len(q) - 1:
                x, y = q[idx], q[idx + 1]
                return min((round((a + 1) /2 + 0.1) - round((a) /2 + 0.1))* z + dfs(idx + 1, (a + 1) % 2), y - x + dfs(idx + 2, a % 2))
            return 0
                # print(x, y, y -x, z, a, b)
                # if y - x <= z:
                # return min(round((a + 1) /2 + 0.1) * z + b + dfs(idx + 1), round((a) /2 + 0.1) * z + b + y - x + dfs(idx + 2))
                # else:
                #     a += 1
                #     idx += 1
            # return round((a) /2 + 0.1) * z + b
        # def dfs(idx):
        #     a, b = 0, 0
        #     while idx < len(q) - 1:
        #         x, y = q[idx], q[idx + 1]
        #         # print(x, y, y -x, z, a, b)
        #         # if y - x <= z:
        #         return min(round((a + 1) /2 + 0.1) * z + b + dfs(idx + 1), round((a) /2 + 0.1) * z + b + y - x + dfs(idx + 2))
        #         # else:
        #         #     a += 1
        #         #     idx += 1
        #     return round((a) /2 + 0.1) * z + b
            
        N = len(s1)
        q = []
        for ii in range(N):
            if s1[ii] != s2[ii]:
                q.append(ii)
        if len(q) % 2:
            return -1
        # print(q)
        return dfs(0, 0)