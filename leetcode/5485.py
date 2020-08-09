# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-09 10:24:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-09 10:24:36

"""
5485. 找出最长的超赞子字符串 显示英文描述 
通过的用户数172
尝试过的用户数515
用户总通过次数197
用户总提交次数1098
题目难度Hard
给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。

「超赞子字符串」需满足满足下述两个条件：

该字符串是 s 的一个非空子字符串
进行任意次数的字符交换重新排序后，该字符串可以变成一个回文字符串
 

示例 1：

输入：s = "3242415"
输出：5
解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
示例 2：

输入：s = "12345678"
输出：1
示例 3：

输入：s = "213123"
输出：6
解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
示例 4：

输入：s = "00"
输出：2
 

提示：

1 <= s.length <= 10^5
s 仅由数字组成
"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        now, res, dp = 0, 0, {}
        dp[0] = -1
        for ii, jj in enumerate(s):
            jj = int(jj)
            now ^= 1 << jj
            if now not in dp:
                dp[now] = ii
            res = max(ii - dp[now], res)
            for kk in range(10):
                tmp = now ^ (1 << kk)
                if tmp in dp:
                    res = max(ii - dp[tmp], res)
        return res
