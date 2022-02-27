# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-02-21 20:11:31
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-02-21 20:12:01
"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2
 

进阶：

尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
通过次数456,093提交次数685,135
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c, vote = nums[0], 1
        for ii in range(1, len(nums)):
            if nums[ii] == c:
                vote += 1
            else:
                vote -= 1
            if vote == 0:
                c = nums[ii]
                vote = 1
        return c
