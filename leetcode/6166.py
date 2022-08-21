# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-08-21 14:05:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-08-21 14:05:15

"""
6166. 最大回文数字 显示英文描述 
通过的用户数2
尝试过的用户数5
用户总通过次数2
用户总提交次数6
题目难度Medium
给你一个仅由数字（0 - 9）组成的字符串 num 。

请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。

注意：

你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
数字可以重新排序。
 

示例 1：

输入：num = "444947137"
输出："7449447"
解释：
从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
可以证明 "7449447" 是能够形成的最大回文整数。
示例 2：

输入：num = "00009"
输出："9"
解释：
可以证明 "9" 能够形成的最大回文整数。
注意返回的整数不应含前导零。
 

提示：

1 <= num.length <= 105
num 由数字（0 - 9）组成
"""
class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        a, b = [], ""
        for ii in range(9, -1, -1):
            if ii == 0:
                if not a:
                    continue
            jj = c.get(str(ii), 0)
            n = jj // 2
            a.extend([str(ii)] * n)
            c[str(ii)] -= n * 2
            # print(a, n, c)
        for ii in range(9, -1, -1):
            jj = c.get(str(ii), 0)
            # print(c, str(ii), jj)
            if jj > 0 and not b:
                b = str(ii)
                break
        a = "".join(a)
        return a + b + a[::-1]
            