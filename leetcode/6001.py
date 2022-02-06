# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-02-06 12:36:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-02-06 12:37:06

"""
6001. 重排数字的最小值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个整数 num 。重排 num 中的各位数字，使其值 最小化 且不含 任何 前导零。

返回不含前导零且值最小的重排数字。

注意，重排各位数字后，num 的符号不会改变。

 

示例 1：

输入：num = 310
输出：103
解释：310 中各位数字的可行排列有：013、031、103、130、301、310 。
不含任何前导零且值最小的重排数字是 103 。
示例 2：

输入：num = -7605
输出：-7650
解释：-7605 中各位数字的部分可行排列为：-7650、-6705、-5076、-0567。
不含任何前导零且值最小的重排数字是 -7650 。
 

提示：

-1015 <= num <= 1015

"""


class Solution:
    def smallestNumber(self, num: int) -> int:
        flag = bool(num < 0)
        s = sorted(str(abs(num)), reverse=flag)
        idx = 0
        if s[0] == "0":
            while idx < len(s) and s[idx] == "0":
                idx += 1
            if idx < len(s):
                s[0], s[idx] = s[idx], s[0]
        res = int("".join(s))
        return res * (-1 if flag else 1)
