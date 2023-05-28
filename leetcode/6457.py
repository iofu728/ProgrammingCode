# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-05-28 11:45:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-05-28 11:46:06

"""
6457. 移除字符串中的尾随零 显示英文描述 
通过的用户数1185
尝试过的用户数1230
用户总通过次数1186
用户总提交次数1263
题目难度Easy
给你一个用字符串表示的正整数 num ，请你以字符串形式返回不含尾随零的整数 num 。

 

示例 1：

输入：num = "51230100"
输出："512301"
解释：整数 "51230100" 有 2 个尾随零，移除并返回整数 "512301" 。
示例 2：

输入：num = "123"
输出："123"
解释：整数 "123" 不含尾随零，返回整数 "123" 。
 

提示：

1 <= num.length <= 1000
num 仅由数字 0 到 9 组成
num 不含前导零
"""
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while num and num[-1] == "0":
            num = num[:-1]
        return num