# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-12-01 11:25:26
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-12-01 11:25:50

"""
100501. 仅含置位位的最小整数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个正整数 n。

返回 大于等于 n 且二进制表示仅包含 置位 位的 最小 整数 x 。

置位 位指的是二进制表示中值为 1 的位。

 

示例 1：

输入： n = 5

输出： 7

解释：

7 的二进制表示是 "111"。

示例 2：

输入： n = 10

输出： 15

解释：

15 的二进制表示是 "1111"。

示例 3：

输入： n = 3

输出： 3

解释：

3 的二进制表示是 "11"。

 

提示：

1 <= n <= 1000
"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        for ii in range(11):
            if 2 ** ii - 1 >= n:
                return 2 ** ii - 1
            
        