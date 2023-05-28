# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-05-28 11:46:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-05-28 11:46:53

"""
6455. 使所有字符相等的最小成本 显示英文描述 
通过的用户数8
尝试过的用户数9
用户总通过次数9
用户总提交次数11
题目难度Medium
给你一个下标从 0 开始、长度为 n 的二进制字符串 s ，你可以对其执行两种操作：

选中一个下标 i 并且反转从下标 0 到下标 i（包括下标 0 和下标 i ）的所有字符，成本为 i + 1 。
选中一个下标 i 并且反转从下标 i 到下标 n - 1（包括下标 i 和下标 n - 1 ）的所有字符，成本为 n - i 。
返回使字符串内所有字符 相等 需要的 最小成本 。

反转 字符意味着：如果原来的值是 '0' ，则反转后值变为 '1' ，反之亦然。

 

示例 1：

输入：s = "0011"
输出：2
解释：执行第二种操作，选中下标 i = 2 ，可以得到 s = "0000" ，成本为 2 。可以证明 2 是使所有字符相等的最小成本。
示例 2：

输入：s = "010101"
输出：9
解释：执行第一种操作，选中下标 i = 2 ，可以得到 s = "101101" ，成本为 3 。
执行第一种操作，选中下标 i = 1 ，可以得到 s = "011101" ，成本为 2 。
执行第一种操作，选中下标 i = 0 ，可以得到 s = "111101" ，成本为 1 。
执行第二种操作，选中下标 i = 4 ，可以得到 s = "111110" ，成本为 2 。
执行第一种操作，选中下标 i = 5 ，可以得到 s = "111111" ，成本为 1 。
使所有字符相等的总成本等于 9 。可以证明 9 是使所有字符相等的最小成本。 
 

提示：

1 <= s.length == n <= 105
s[i] 为 '0' 或 '1'

"""
class Solution:
    def minimumCost(self, s: str) -> int:
        N = len(s)
        def get_x(tag):
            ss = []
            dirs = 0
            idx = 0
            
            while idx < N:
                start = idx
                t = s[idx]
                while idx + 1 < N and s[idx + 1] == t:
                    idx += 1
                ss.append((start, idx, t))
                idx += 1

            M = len(ss)
            xx, yy = [0] * (M + 1), [0] * (M + 1)
            for ii in range(M):
                start, e, t = ss[ii]
                xx[ii + 1] = xx[ii] + e + 1
            for ii in range(M - 1, -1, -1):
                start, e, t = ss[ii]
                yy[ii] = yy[ii + 1] + N - start
            res = float("inf")
            # print(xx, yy)
            for ii in range(M):
                start, e, t = ss[ii]
                if t != tag:
                    k = xx[ii + 1] + (yy[ii + 2] if ii + 2 < M + 1 else 0)
                    v = yy[ii] + (xx[ii - 1] if ii - 1 >= 0 else 0)
                    res = min(res, k, v)
                    # print(tag, res, k, v)
            return 0 if float("inf") == res else res
        return min(get_x("0"), get_x("1"))
            
                    
                
                    
                    