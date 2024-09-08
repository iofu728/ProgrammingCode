# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-09-08 12:59:09
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-09-08 13:00:01

"""
100389. 到达数组末尾的最大得分 显示英文描述 
通过的用户数73
尝试过的用户数122
用户总通过次数74
用户总提交次数165
题目难度Medium
给你一个长度为 n 的整数数组 nums 。

你的目标是从下标 0 出发，到达下标 n - 1 处。每次你只能移动到 更大 的下标处。

从下标 i 跳到下标 j 的得分为 (j - i) * nums[i] 。

请你返回你到达最后一个下标处能得到的 最大总得分 。

 

示例 1：

输入：nums = [1,3,1,5]

输出：7

解释：

一开始跳到下标 1 处，然后跳到最后一个下标处。总得分为 1 * 1 + 2 * 3 = 7 。

示例 2：

输入：nums = [4,3,1,3,2]

输出：16

解释：

直接跳到最后一个下标处。总得分为 4 * 4 = 16 。

 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        res = 0
        last = 0
        idx = 0
        N = len(nums)
        if N == 1:
            return 0
        while idx < N:
            now = last + 1
            while nums[last] > nums[now] and now + 1 < N:
                now += 1
            res += (now - last) * nums[last]
            last = now
            idx = now + 1
        return res
        # @lru_cache(None)
        # def dp(x):
        #     if x == 0:
        #         return 0
        #     res = 0
        #     for ii in range(x):
        #         res = max(dp(ii) + (x - ii) * nums[ii], res)
        #     return res
        # return dp(len(nums) - 1)