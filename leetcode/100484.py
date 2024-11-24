# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-11-24 13:50:27
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-11-24 13:51:06

"""
100484. 最小正和子数组 显示英文描述 
通过的用户数600
尝试过的用户数736
用户总通过次数603
用户总提交次数917
题目难度Easy
给你一个整数数组 nums 和 两个 整数 l 和 r。你的任务是找到一个长度在 l 和 r 之间（包含）且和大于 0 的 子数组 的 最小 和。

返回满足条件的子数组的 最小 和。如果不存在这样的子数组，则返回 -1。

子数组 是数组中的一个连续 非空 元素序列。

 

示例 1：

输入： nums = [3, -2, 1, 4], l = 2, r = 3

输出： 1

解释：

长度在 l = 2 和 r = 3 之间且和大于 0 的子数组有：

[3, -2] 和为 1
[1, 4] 和为 5
[3, -2, 1] 和为 2
[-2, 1, 4] 和为 3
其中，子数组 [3, -2] 的和为 1，是所有正和中最小的。因此，答案为 1。

示例 2：

输入： nums = [-2, 2, -3, 1], l = 2, r = 3

输出： -1

解释：

不存在长度在 l 和 r 之间且和大于 0 的子数组。因此，答案为 -1。

示例 3：

输入： nums = [1, 2, 3, 4], l = 2, r = 4

输出： 3

解释：

子数组 [1, 2] 的长度为 2，和为 3，是所有正和中最小的。因此，答案为 3。

 

提示：

1 <= nums.length <= 100
1 <= l <= r <= nums.length
-1000 <= nums[i] <= 1000
"""
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = -1
        N = len(nums)
        for x in range(N - l + 1):
            tmp = sum(nums[x:x + l])
            if tmp > 0:
                if res == -1:
                    res = tmp
                else:
                    res = min(res, tmp)
            for y in range(x + l, x + r):
                if y >= N:
                    break
                tmp += nums[y]
                if tmp > 0:
                    if res == -1:
                        res = tmp
                    else:
                        res = min(res, tmp)
        return res
        