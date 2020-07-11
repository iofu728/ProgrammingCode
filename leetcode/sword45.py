# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 11:51:53
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 11:52:20

"""
剑指 Offer 45. 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
通过次数18,656提交次数33,485
"""


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            if a < b:
                return -1
            return 0

        num_str = [str(ii) for ii in nums]
        num_str.sort(key=functools.cmp_to_key(cmp))
        return "".join(num_str)
