# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-03-19 11:40:44
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-03-19 11:41:28

"""
6319. 奇偶位数 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个 正 整数 n 。

用 even 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的偶数下标的个数。

用 odd 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的奇数下标的个数。

返回整数数组 answer ，其中 answer = [even, odd] 。

 

示例 1：

输入：n = 17
输出：[2,0]
解释：17 的二进制形式是 10001 。 
下标 0 和 下标 4 对应的值为 1 。 
共有 2 个偶数下标，0 个奇数下标。
示例 2：

输入：n = 2
输出：[0,1]
解释：2 的二进制形式是 10 。 
下标 1 对应的值为 1 。 
共有 0 个偶数下标，1 个奇数下标。
 

提示：

1 <= n <= 1000
"""


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        x = bin(n)[2::][::-1]
        m, n = 0, 0
        for ii, jj in enumerate(x):
            if jj == "1":
                if ii % 2 == 0:
                    m += 1
                else:
                    n += 1
        return [m, n]
