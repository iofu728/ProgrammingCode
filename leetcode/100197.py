# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-02-25 23:59:12
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-02-25 23:59:22

"""
100197. 标记所有下标的最早秒数 II 显示英文描述 
通过的用户数0
尝试过的用户数5
用户总通过次数0
用户总提交次数10
题目难度Hard
给你两个下标从 1 开始的整数数组 nums 和 changeIndices ，数组的长度分别为 n 和 m 。

一开始，nums 中所有下标都是未标记的，你的任务是标记 nums 中 所有 下标。

从第 1 秒到第 m 秒（包括 第 m 秒），对于每一秒 s ，你可以执行以下操作 之一 ：

选择范围 [1, n] 中的一个下标 i ，并且将 nums[i] 减少 1 。
将 nums[changeIndices[s]] 设置成任意的 非负 整数。
选择范围 [1, n] 中的一个下标 i ， 满足 nums[i] 等于 0, 并 标记 下标 i 。
什么也不做。
请你返回范围 [1, m] 中的一个整数，表示最优操作下，标记 nums 中 所有 下标的 最早秒数 ，如果无法标记所有下标，返回 -1 。

 

示例 1：

输入：nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]
输出：6
解释：这个例子中，我们总共有 7 秒。按照以下操作标记所有下标：
第 1 秒：将 nums[changeIndices[1]] 变为 0 。nums 变为 [0,2,3] 。
第 2 秒：将 nums[changeIndices[2]] 变为 0 。nums 变为 [0,2,0] 。
第 3 秒：将 nums[changeIndices[3]] 变为 0 。nums 变为 [0,0,0] 。
第 4 秒：标记下标 1 ，因为 nums[1] 等于 0 。
第 5 秒：标记下标 2 ，因为 nums[2] 等于 0 。
第 6 秒：标记下标 3 ，因为 nums[3] 等于 0 。
现在所有下标已被标记。
最早可以在第 6 秒标记所有下标。
所以答案是 6 。
示例 2：

输入：nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2]
输出：7
解释：这个例子中，我们总共有 8 秒。按照以下操作标记所有下标：
第 1 秒：标记下标 1 ，因为 nums[1] 等于 0 。
第 2 秒：标记下标 2 ，因为 nums[2] 等于 0 。
第 3 秒：将 nums[4] 减少 1 。nums 变为 [0,0,1,1] 。
第 4 秒：将 nums[4] 减少 1 。nums 变为 [0,0,1,0] 。
第 5 秒：将 nums[3] 减少 1 。nums 变为 [0,0,0,0] 。
第 6 秒：标记下标 3 ，因为 nums[3] 等于 0 。
第 7 秒：标记下标 4 ，因为 nums[4] 等于 0 。
现在所有下标已被标记。
最早可以在第 7 秒标记所有下标。
所以答案是 7 。
示例 3：

输入：nums = [1,2,3], changeIndices = [1,2,3]
输出：-1
解释：这个例子中，无法标记所有下标，因为我们没有足够的秒数。
所以答案是 -1 。
 

提示：

1 <= n == nums.length <= 5000
0 <= nums[i] <= 109
1 <= m == changeIndices.length <= 5000
1 <= changeIndices[i] <= n
"""
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        first_idx = [-1] * len(nums)
        for i in range(len(changeIndices)):
            if first_idx[changeIndices[i]-1] == -1:
                first_idx[changeIndices[i]-1] = i

        for i, num in enumerate(nums):
            if num <= 1:
                first_idx[i] = -1

        default_needs = sum(nums) + len(nums)

        def is_possible(k):
            left = 0
            h = []

            pos_count = 0
            flag = False
            for j in range(k, -1, -1):
                if flag:
                    pos_count += 1
                    flag = False
                else:
                    flag = True

                left += 1

                i1 = first_idx[changeIndices[j]-1]
                if i1 == j:
                    heapq.heappush(h, [nums[changeIndices[j]-1] - 1, changeIndices[j]-1])
                if len(h) > pos_count:
                    heapq.heappop(h)

            return default_needs - sum(h1[0] for h1 in h) <= left

            ans = 0
            return ans

        l, r = len(nums)-1, len(changeIndices)-1
        while l < r:
            m = (l + r) // 2
            if is_possible(m):
                r = m
            else:
                l = m + 1
        if l > r or not is_possible(l):
            return -1
        return l+1
