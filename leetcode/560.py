# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-05-15 22:16:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-05-15 22:17:03

"""
560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
通过次数44,492提交次数101,158
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        c_map = {}
        tmp, res = 0, 0
        for ii in nums:
            tmp += ii
            if tmp == k:
                res += 1
            if tmp - k in c_map:
                res += c_map[tmp - k]
            c_map[tmp] = c_map.get(tmp, 0) + 1
        return res
