# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-12-26 11:16:22
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-12-26 11:16:36

"""
5963. 反转两次的数字 显示英文描述 
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
反转 一个整数意味着倒置它的所有位。

例如，反转 2021 得到 1202 。反转 12300 得到 321 ，不保留前导零 。
给你一个整数 num ，反转 num 得到 reversed1 ，接着反转 reversed1 得到 reversed2 。如果 reversed2 等于 num ，返回 true ；否则，返回 false 。

 

示例 1：

输入：num = 526
输出：true
解释：反转 num 得到 625 ，接着反转 625 得到 526 ，等于 num 。
示例 2：

输入：num = 1800
输出：false
解释：反转 num 得到 81 ，接着反转 81 得到 18 ，不等于 num 。 
示例 3：

输入：num = 0
输出：true
解释：反转 num 得到 0 ，接着反转 0 得到 0 ，等于 num 。
 

提示：

0 <= num <= 106
"""
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        if num[-1] == "0" and len(num) != 1:
            return False
        return True