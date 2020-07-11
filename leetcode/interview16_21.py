# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-07-11 14:14:52
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-07-11 14:15:06

"""
面试题 16.21. 交换和
给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。

返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。

示例:

输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
输出: [1, 3]
示例:

输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
输出: []
提示：

1 <= array1.length, array2.length <= 100000
通过次数2,743提交次数6,136
"""


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        diff = sum(array1) - sum(array2)
        if diff & 1:
            return []
        diff >>= 1
        s2 = set(array2)
        for ii in set(array1):
            if ii - diff in s2:
                return [ii, ii - diff]
        return []
