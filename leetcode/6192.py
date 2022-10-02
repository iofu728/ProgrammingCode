# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-02 12:55:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-02 12:55:17

"""
6192. 公因子的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。

如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。

 

示例 1：

输入：a = 12, b = 6
输出：4
解释：12 和 6 的公因子是 1、2、3、6 。
示例 2：

输入：a = 25, b = 30
输出：2
解释：25 和 30 的公因子是 1、5 。
 

提示：

1 <= a, b <= 1000
"""
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return len([1 for ii in range(1, min(a, b, 1000) + 1) if a % ii == 0 and b % ii == 0])