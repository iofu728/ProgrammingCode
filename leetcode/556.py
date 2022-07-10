# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-07-03 11:26:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-07-03 11:26:30

"""
556. 下一个更大元素 III
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

 

示例 1：

输入：n = 12
输出：21
示例 2：

输入：n = 21
输出：-1
 

提示：

1 <= n <= 231 - 1
通过次数25,335提交次数72,629
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        idx = len(nums) - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1
        if idx < 0:
            return -1
        jj = len(nums) - 1
        while jj >= 0 and nums[idx] >= nums[jj]:
            jj -= 1
        nums[idx], nums[jj] = nums[jj], nums[idx]
        nums[idx + 1:] = nums[idx + 1:][::-1]
        res = int("".join(nums))
        return res if res < 2 ** 31 else -1
