# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-25 11:10:51
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-25 11:11:05

"""
6471. 得到整数零需要执行的最少操作数 显示英文描述 
通过的用户数0
尝试过的用户数1
用户总通过次数0
用户总提交次数1
题目难度Medium
给你两个整数：num1 和 num2 。

在一步操作中，你需要从范围 [0, 60] 中选出一个整数 i ，并从 num1 减去 2i + num2 。

请你计算，要想使 num1 等于 0 需要执行的最少操作数，并以整数形式返回。

如果无法使 num1 等于 0 ，返回 -1 。

 

示例 1：

输入：num1 = 3, num2 = -2
输出：3
解释：可以执行下述步骤使 3 等于 0 ：
- 选择 i = 2 ，并从 3 减去 22 + (-2) ，num1 = 3 - (4 + (-2)) = 1 。
- 选择 i = 2 ，并从 1 减去 22 + (-2) ，num1 = 1 - (4 + (-2)) = -1 。
- 选择 i = 0 ，并从 -1 减去 20 + (-2) ，num1 = (-1) - (1 + (-2)) = 0 。
可以证明 3 是需要执行的最少操作数。
示例 2：

输入：num1 = 5, num2 = 7
输出：-1
解释：可以证明，执行操作无法使 5 等于 0 。
 

提示：

1 <= num1 <= 109
-109 <= num2 <= 109
"""
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 0
        while 2 ** 61 > num1 - k * num2 > 0:
            c = num1 - k * num2
            y = bin(c)[2:].count("1")
            if k >= y and c >= k:
                return k
            k += 1
        return -1
            