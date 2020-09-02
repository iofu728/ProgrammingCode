# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-09-02 16:44:02
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-09-02 16:44:15

"""
面试题 10.11. 峰与谷
在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 6, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。

示例:

输入: [5, 3, 1, 2, 3]
输出: [5, 1, 3, 2, 3]
提示：

nums.length <= 10000
通过次数2,968提交次数4,514
"""


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for ii in range(len(nums)):
            if (ii >> 1 << 1 == ii and nums[ii] < nums[ii - 1]) or (
                ii >> 1 << 1 != ii and nums[ii] > nums[ii - 1]
            ):
                nums[ii], nums[ii - 1] = nums[ii - 1], nums[ii]
