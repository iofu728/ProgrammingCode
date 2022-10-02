# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-02 12:55:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-02 12:56:05

"""
6194. 最小 XOR 显示英文描述 
通过的用户数1
尝试过的用户数2
用户总通过次数1
用户总提交次数2
题目难度Medium
给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：

x 的置位数和 num2 相同，且
x XOR num1 的值 最小
注意 XOR 是按位异或运算。

返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。

整数的 置位数 是其二进制表示中 1 的数目。

 

示例 1：

输入：num1 = 3, num2 = 5
输出：3
解释：
num1 和 num2 的二进制表示分别是 0011 和 0101 。
整数 3 的置位数与 num2 相同，且 3 XOR 3 = 0 是最小的。
示例 2：

输入：num1 = 1, num2 = 12
输出：3
解释：
num1 和 num2 的二进制表示分别是 0001 和 1100 。
整数 3 的置位数与 num2 相同，且 3 XOR 1 = 2 是最小的。
 

提示：

1 <= num1, num2 <= 109
"""
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        x, y = bin(num1).count("1"), bin(num2).count("1")

        if x <= y:
            a, b = "0", "1"
        else:
            a, b = "1", "0"
        n = abs(x - y)
        res = list(bin(num1)[2:])
        idx = len(res) - 1
        while n > 0 and idx >= 0:
            if res[idx] == a:
                res[idx] =  b
                n -= 1
            idx -= 1
        res = "".join(res)
        if n:
            res = b * n + res
        return int(res, 2)
            
        