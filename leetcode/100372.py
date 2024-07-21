# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-07-21 13:03:57
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-07-21 13:04:07

"""
100372. 使两个整数相等的位更改次数 显示英文描述 
通过的用户数1995
尝试过的用户数2110
用户总通过次数2049
用户总提交次数2913
题目难度Easy
给你两个正整数 n 和 k。

你可以选择 n 的 二进制表示 中任意一个值为 1 的位，并将其改为 0。

返回使得 n 等于 k 所需要的更改次数。如果无法实现，返回 -1。

 

示例 1：

输入： n = 13, k = 4

输出： 2

解释：
最初，n 和 k 的二进制表示分别为 n = (1101)2 和 k = (0100)2，

我们可以改变 n 的第一位和第四位。结果整数为 n = (0100)2 = k。

示例 2：

输入： n = 21, k = 21

输出： 0

解释：
n 和 k 已经相等，因此不需要更改。

示例 3：

输入： n = 14, k = 13

输出： -1

解释：
无法使 n 等于 k。

 

提示：

1 <= n, k <= 106
"""
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        a = bin(n)[2:]
        b = bin(k)[2:]
        if len(a) < len(b):
            return -1
        k = len(a) - len(b)
        res = 0
        for ii in range(k):
            if a[ii] == "1":
                res += 1
            
        a = a[k:]
        for i, j in zip(a, b):
            if i == j:
                continue
            if i == "1":
                res += 1
            else:
                return -1
        return res