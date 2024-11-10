# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-11-10 13:13:42
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-11-10 13:13:57

"""
100463. 检测相邻递增子数组 II 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Medium
给你一个由 n 个整数组成的数组 nums ，请你找出 k 的 最大值，使得存在 两个 相邻 且长度为 k 的 严格递增 子数组。具体来说，需要检查是否存在从下标 a 和 b (a < b) 开始的 两个 子数组，并满足下述全部条件：

这两个子数组 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是 严格递增 的。
这两个子数组必须是 相邻的，即 b = a + k。
返回 k 的 最大可能 值。

子数组 是数组中的一个连续 非空 的元素序列。

 

示例 1：

输入：nums = [2,5,7,8,9,2,3,4,3,1]

输出：3

解释：

从下标 2 开始的子数组是 [7, 8, 9]，它是严格递增的。
从下标 5 开始的子数组是 [2, 3, 4]，它也是严格递增的。
这两个子数组是相邻的，因此 3 是满足题目条件的 最大 k 值。
示例 2：

输入：nums = [1,2,3,4,4,4,4,5,6,7]

输出：2

解释：

从下标 0 开始的子数组是 [1, 2]，它是严格递增的。
从下标 2 开始的子数组是 [3, 4]，它也是严格递增的。
这两个子数组是相邻的，因此 2 是满足题目条件的 最大 k 值。
 

提示：

2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
"""
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        N = len(nums)
        last = [-1]
        for ii in range(1, N):
            if nums[ii] <= nums[ii - 1]:
                now = ii - 1
                ans = max(ans, (now - last[-1]) // 2)
                if len(last) >= 2:
                    ans = max(ans, min(now - last[-1], last[-1] - last[-2]))
                last.append(now)
        now = N - 1
        ans = max(ans, (now - last[-1]) // 2)
        if len(last) >= 2:
            ans = max(ans, min(now - last[-1], last[-1] - last[-2]))
        return ans