# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-18 12:25:19
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-18 12:25:35

"""
100409. 找出最大的 N 位 K 回文数 显示英文描述 
通过的用户数0
尝试过的用户数9
用户总通过次数0
用户总提交次数11
题目难度Hard
给你两个 正整数 n 和 k。

如果整数 x 满足以下全部条件，则该整数是一个 k 回文数：

x 是一个 回文数。
x 可以被 k 整除。
以字符串形式返回 最大的  n 位 k 回文数。

注意，该整数 不 含前导零。

 

示例 1：

输入： n = 3, k = 5

输出： "595"

解释：

595 是最大的 3 位 k 回文数。

示例 2：

输入： n = 1, k = 4

输出： "8"

解释：

1 位 k 回文数只有 4 和 8。

示例 3：

输入： n = 5, k = 6

输出： "89898"

 

提示：

1 <= n <= 105
1 <= k <= 9
"""
sys.set_int_max_str_digits(2 * 10 ** 5 + 1)
            
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        m = n // 2
        if n == 1:
            for ii in range(9, -1, -1):
                if ii % k == 0:
                    return str(ii)
        # print(m)
        if n % 2 == 0:
            for ii in range(10 ** m - 1, 10**(m-1) - 1, -1):
                num = str(ii) + str(ii)[::-1]
                if k == 5:
                    num = "5" + num[1:]
                    num = num[:-1] + '5'
                elif k == 8 and n >= 3:
                    num = "888" + num[3:]
                    num = num[:-3] + "888"
                    
                elif k == 4 and n > 2:
                    num = "88" + num[2:]
                    num = num[:-2] + "88"
                elif k in [2, 6] and n > 2:
                    num = "8" + num[1:]
                    num = num[:-1] + "8"
                if int(num) % k == 0:
                    return num
        else:
            for ii in range(10 ** m - 1, 10**(m-1) - 1, -1):
                for jj in range(9, -1, -1):
                    num = str(ii) + str(jj) + str(ii)[::-1]
                    if k == 5:
                        num = "5" + num[1:]
                        num = num[:-1] + '5'
                    elif k == 8 and n >= 3:
                        num = "888" + num[3:]
                        num = num[:-3] + "888"
                    elif k == 4 and n > 2:
                        num = "88" + num[2:]
                        num = num[:-2] + "88"
                    elif k in [2, 6] and n > 2:
                        num = "8" + num[1:]
                        num = num[:-1] + "8"
                    if int(num) % k == 0:
                        return num
        