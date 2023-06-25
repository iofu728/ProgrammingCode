# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-06-25 11:11:15
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-06-25 11:11:25

"""
6910. 将数组划分成若干好子数组的方式 显示英文描述 
通过的用户数256
尝试过的用户数289
用户总通过次数256
用户总提交次数473
题目难度Medium
给你一个二元数组 nums 。

如果数组中的某个子数组 恰好 只存在 一 个值为 1 的元素，则认为该子数组是一个 好子数组 。

请你统计将数组 nums 划分成若干 好子数组 的方法数，并以整数形式返回。由于数字可能很大，返回其对 109 + 7 取余 之后的结果。

子数组是数组中的一个连续 非空 元素序列。

 

示例 1：

输入：nums = [0,1,0,0,1]
输出：3
解释：存在 3 种可以将 nums 划分成若干好子数组的方式：
- [0,1] [0,0,1]
- [0,1,0] [0,1]
- [0,1,0,0] [1]
示例 2：

输入：nums = [0,1,0]
输出：1
解释：存在 1 种可以将 nums 划分成若干好子数组的方式：
- [0,1,0]
 

提示：

1 <= nums.length <= 105
0 <= nums[i] <= 1
"""
class Solution:
    MODS = 10 ** 9 + 7
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        N = len(nums)
        if 1 not in set(nums):
            return 0
        idx = []
        res = 1
        for ii, jj in enumerate(nums):
            if jj == 1:
                idx.append(ii)
        for jj in range(1, len(idx)):
            res = (res * (idx[jj] - idx[jj - 1])) % self.MODS
        return res