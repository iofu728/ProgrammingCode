# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-11-10 13:12:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-11-10 13:13:05

"""
100457. 检测相邻递增子数组 I 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个由 n 个整数组成的数组 nums 和一个整数 k，请你确定是否存在 两个 相邻 且长度为 k 的 严格递增 子数组。具体来说，需要检查是否存在从下标 a 和 b (a < b) 开始的 两个 子数组，并满足下述全部条件：

这两个子数组 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是 严格递增 的。
这两个子数组必须是 相邻的，即 b = a + k。
如果可以找到这样的 两个 子数组，请返回 true；否则返回 false。

子数组 是数组中的一个连续 非空 的元素序列。

 

示例 1：

输入：nums = [2,5,7,8,9,2,3,4,3,1], k = 3

输出：true

解释：

从下标 2 开始的子数组为 [7, 8, 9]，它是严格递增的。
从下标 5 开始的子数组为 [2, 3, 4]，它也是严格递增的。
两个子数组是相邻的，因此结果为 true。
示例 2：

输入：nums = [1,2,3,4,4,4,4,5,6,7], k = 5

输出：false

 

提示：

2 <= nums.length <= 100
1 <= 2 * k <= nums.length
-1000 <= nums[i] <= 1000
"""
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        last = [-1]
        for ii in range(1, N):
            if nums[ii] <= nums[ii - 1]:
                now = ii - 1
                # print(now, last)
                if now - last[-1] >= 2 * k:
                    return True
                if now - last[-1] >= k and len(last) >= 2 and last[-1] - last[-2] >= k:
                    return True
                last.append(now)
        now = N - 1
        if now - last[-1] >= 2 * k:
            return True
        if now - last[-1] >= k and len(last) >= 2 and last[-1] - last[-2] >= k:
            return True
        return False
