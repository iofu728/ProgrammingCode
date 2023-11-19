# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-11-19 12:18:52
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-11-19 12:19:59

"""
100131. 使三个字符串相等 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你三个字符串 s1、s2 和 s3。 你可以根据需要对这三个字符串执行以下操作 任意次数 。

在每次操作中，你可以选择其中一个长度至少为 2 的字符串 并删除其 最右位置上 的字符。

如果存在某种方法能够使这三个字符串相等，请返回使它们相等所需的 最小 操作次数；否则，返回 -1。

 

示例 1：

输入：s1 = "abc"，s2 = "abb"，s3 = "ab"
输出：2
解释：对 s1 和 s2 进行一次操作后，可以得到三个相等的字符串。
可以证明，不可能用少于两次操作使它们相等。
示例 2：

输入：s1 = "dac"，s2 = "bac"，s3 = "cac"
输出：-1
解释：因为 s1 和 s2 的最左位置上的字母不相等，所以无论进行多少次操作，它们都不可能相等。因此答案是 -1 。
 

提示：

1 <= s1.length, s2.length, s3.length <= 100
s1、s2 和 s3 仅由小写英文字母组成。

"""
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        res = 0
        N = min(len(s1), len(s2), len(s3))
        for ii in range(N):
            if not (s1[ii] == s2[ii] == s3[ii]):
                break
            res += 1
        if res == 0:
            return -1
        return len(s1) - res + len(s2) - res  + len(s3) - res 