# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-28 23:52:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-28 23:53:32

"""
面试题56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

限制：

2 <= nums <= 10000

通过次数24,687提交次数33,685
"""
from functools import reduce


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        b, q = reduce(lambda x, y: x ^ y, nums), 1
        while q & b == 0:
            q <<= 1
        a, b = 0, 0
        for ii in nums:
            if ii & q:
                a ^= ii
            else:
                b ^= ii
        return [a, b]
