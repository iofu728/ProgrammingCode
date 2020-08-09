# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-09 10:39:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-09 11:20:56

"""
5484. 找出第 N 个二进制字符串中的第 K 位 显示英文描述 
通过的用户数25
尝试过的用户数34
用户总通过次数25
用户总提交次数39
题目难度Medium
给你两个正整数 n 和 k，二进制字符串  Sn 的形成规则如下：

S1 = "0"
当 i > 1 时，Si = Si-1 + "1" + reverse(invert(Si-1))
其中 + 表示串联操作，reverse(x) 返回反转 x 后得到的字符串，而 invert(x) 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）

例如，符合上述描述的序列的前 4 个字符串依次是：

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
请你返回  Sn 的 第 k 位字符 ，题目数据保证 k 一定在 Sn 长度范围以内。

 

示例 1：

输入：n = 3, k = 1
输出："0"
解释：S3 为 "0111001"，其第 1 位为 "0" 。
示例 2：

输入：n = 4, k = 11
输出："1"
解释：S4 为 "011100110110001"，其第 11 位为 "1" 。
示例 3：

输入：n = 1, k = 1
输出："0"
示例 4：

输入：n = 2, k = 3
输出："1"
 

提示：

1 <= n <= 20
1 <= k <= 2n - 1
"""
import math


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        need = math.ceil(math.log2(k + 1))
        now, ss = 1, "0"
        if k == 1:
            return "0"
        if 2 ** (need - 1) == k:
            return "1"
        idx = 2 ** (need) - k if k > 2 ** (need - 1) - 1 else k
        res = 1
        while idx > 1:
            # print(res, idx, need)
            res ^= 1
            need = math.ceil(math.log2(idx + 1))
            if 2 ** (need - 1) == idx:
                # res ^= 1
                break

            idx = 2 ** (need) - idx if idx > 2 ** (need - 1) else idx
        return str(res)
