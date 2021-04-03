# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-04-03 22:49:01
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-04-03 22:49:12

"""
5708. 统计一个数组中好对子的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个数组 nums ，数组中只包含非负整数。定义 rev(x) 的值为将整数 x 各个数字位反转得到的结果。比方说 rev(123) = 321 ， rev(120) = 21 。我们称满足下面条件的下标对 (i, j) 是 好的 ：

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
请你返回好下标对的数目。由于结果可能会很大，请将结果对 109 + 7 取余 后返回。

 

示例 1：

输入：nums = [42,11,1,97]
输出：2
解释：两个坐标对为：
 - (0,3)：42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121 。
 - (1,2)：11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12 。
示例 2：

输入：nums = [13,10,35,24,76]
输出：4
 

提示：

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
from collections import defaultdict


class Solution:
    MODS = 10 ** 9 + 7

    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num: int):
            res = 0
            while num > 0:
                res = res * 10 + num % 10
                num //= 10
            return res

        N = len(nums)
        c = defaultdict(int)
        for num in nums:
            tmp = num - rev(num)
            c[tmp] += 1
        res = 0
        print(c)
        for k, v in c.items():
            # if k:
            # res += v * c.get(-k, 0)
            # else:
            res += (v * (v - 1)) // 2
            res %= self.MODS
        return res
