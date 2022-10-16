# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-16 12:25:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-16 12:26:08

"""
6219. 反转之后的数字和 显示英文描述 
通过的用户数7
尝试过的用户数10
用户总通过次数7
用户总提交次数12
题目难度Medium
给你一个 非负 整数 num 。如果存在某个 非负 整数 k 满足 k + reverse(k) = num  ，则返回 true ；否则，返回 false 。

reverse(k) 表示 k 反转每个数位后得到的数字。

 

示例 1：

输入：num = 443
输出：true
解释：172 + 271 = 443 ，所以返回 true 。
示例 2：

输入：num = 63
输出：false
解释：63 不能表示为非负整数及其反转后数字之和，返回 false 。
示例 3：

输入：num = 181
输出：true
解释：140 + 041 = 181 ，所以返回 true 。注意，反转后的数字可能包含前导零。
 

提示：

0 <= num <= 105
"""
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def convert(a):
            return int(str(a)[::-1])
        for ii in range(num, num // 2 - 2, -1):
            if ii < 0:
                break
            if ii + convert(ii) == num:
                return True
        return False