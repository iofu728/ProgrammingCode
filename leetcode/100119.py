# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-11-19 12:20:42
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-11-19 12:20:50

"""
100119. 最大异或乘积 显示英文描述 
通过的用户数0
尝试过的用户数2
用户总通过次数0
用户总提交次数2
题目难度Medium
给你三个整数 a ，b 和 n ，请你返回 (a XOR x) * (b XOR x) 的 最大值 且 x 需要满足 0 <= x < 2n。

由于答案可能会很大，返回它对 109 + 7 取余 后的结果。

注意，XOR 是按位异或操作。

 

示例 1：

输入：a = 12, b = 5, n = 4
输出：98
解释：当 x = 2 时，(a XOR x) = 14 且 (b XOR x) = 7 。所以，(a XOR x) * (b XOR x) = 98 。
98 是所有满足 0 <= x < 2n 中 (a XOR x) * (b XOR x) 的最大值。
示例 2：

输入：a = 6, b = 7 , n = 5
输出：930
解释：当 x = 25 时，(a XOR x) = 31 且 (b XOR x) = 30 。所以，(a XOR x) * (b XOR x) = 930 。
930 是所有满足 0 <= x < 2n 中 (a XOR x) * (b XOR x) 的最大值。
示例 3：

输入：a = 1, b = 6, n = 3
输出：12
解释： 当 x = 5 时，(a XOR x) = 4 且 (b XOR x) = 3 。所以，(a XOR x) * (b XOR x) = 12 。
12 是所有满足 0 <= x < 2n 中 (a XOR x) * (b XOR x) 的最大值。
 

提示：

0 <= a, b < 250
0 <= n <= 50
"""
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if a < b:
            a, b = b, a
        a, b = bin(a)[2:], bin(b)[2:]
        x, y = "", ""
        flag = True
        for jj in range(n - len(a), 0):
            # print(jj, n - len(a))
            x += a[jj - n + len(a)]
            if jj -( n - len(b)) >= 0:
                y += b[jj - (n - len(b))]
                if x > y:
                    flag = False
            else:
                flag = False
        for ii in range(n):
            i = ii - (n - len(a))
            j = ii - (n - len(b))
            xx, yy = a[i] if i >= 0 else "0", b[j] if j >= 0 else "0"
            if xx == yy:
                x += "1"
                y += "1"
            else:
                if flag:
                    x += "1"
                    y += "0"
                    flag = False
                else:
                    x += "0"
                    y += "1"
        # print(x, y)
        return int(x, 2) * int(y, 2) % (10 ** 9 + 7)
                