# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-07-21 13:04:56
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-07-21 13:05:05

"""
100329. 使数组等于目标数组所需的最少操作次数 显示英文描述 
通过的用户数231
尝试过的用户数399
用户总通过次数250
用户总提交次数587
题目难度Hard
给你两个长度相同的正整数数组 nums 和 target。

在一次操作中，你可以选择 nums 的任何子数组，并将该子数组内的每个元素的值增加或减少 1。

返回使 nums 数组变为 target 数组所需的 最少 操作次数。

 

示例 1：

输入： nums = [3,5,1,2], target = [4,6,2,4]

输出： 2

解释：

执行以下操作可以使 nums 等于 target：
- nums[0..3] 增加 1，nums = [4,6,2,3]。
- nums[3..3] 增加 1，nums = [4,6,2,4]。

示例 2：

输入： nums = [1,3,2], target = [2,1,4]

输出： 5

解释：

执行以下操作可以使 nums 等于 target：
- nums[0..0] 增加 1，nums = [2,3,2]。
- nums[1..1] 减少 1，nums = [2,2,2]。
- nums[1..1] 减少 1，nums = [2,1,2]。
- nums[2..2] 增加 1，nums = [2,1,3]。
- nums[2..2] 增加 1，nums = [2,1,4]。

 

提示：

1 <= nums.length == target.length <= 105
1 <= nums[i], target[i] <= 108
"""
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        a = [x - y for x, y in zip(nums, target)]
        s = [a[0]]
        for x, y in pairwise(a):
            s.append(y - x)
        pos = [x for x in s if x > 0] + [0]
        neg = [-x for x in s if x < 0] + [0]
        return max(sum(pos),sum(neg))
            