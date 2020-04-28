# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-24 15:08:42
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-24 15:09:06

"""
面试题51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5

限制：

0 <= 数组长度 <= 50000

通过次数12,396提交次数28,386
"""


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return 0
        mid, idx = N // 2, 0
        left, right = nums[:mid], nums[mid:]
        res = self.reversePairs(left) + self.reversePairs(right)
        left, right = sorted(left), sorted(right)
        # print(left, right)
        for ii in range(N - mid):
            while idx < mid and left[idx] <= right[ii]:
                idx += 1
            res += mid - idx
        return res
