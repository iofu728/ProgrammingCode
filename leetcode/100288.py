# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-05-05 12:48:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-05-05 12:48:50

"""
100288. 使数组中所有元素相等的最小开销 显示英文描述 
通过的用户数8
尝试过的用户数53
用户总通过次数8
用户总提交次数87
题目难度Hard
给你一个整数数组 nums 和两个整数 cost1 和 cost2 。你可以执行以下 任一 操作 任意 次：

从 nums 中选择下标 i 并且将 nums[i] 增加 1 ，开销为 cost1。
选择 nums 中两个 不同 下标 i 和 j ，并且将 nums[1] 和 nums[2] 都 增加 1 ，开销为 cost2 。
你的目标是使数组中所有元素都 相等 ，请你返回需要的 最小开销 之和。

由于答案可能会很大，请你将它对 109 + 7 取余 后返回。

 

示例 1：

输入：nums = [4,1], cost1 = 5, cost2 = 2

输出：15

解释：

执行以下操作可以使数组中所有元素相等：

将 nums[1] 增加 1 ，开销为 5 ，nums 变为 [4,2] 。
将 nums[1] 增加 1 ，开销为 5 ，nums 变为 [4,3] 。
将 nums[1] 增加 1 ，开销为 5 ，nums 变为 [4,4] 。
总开销为 15 。

示例 2：

输入：nums = [2,3,3,3,5], cost1 = 2, cost2 = 1

输出：6

解释：

执行以下操作可以使数组中所有元素相等：

将 nums[0] 和 nums[1] 同时增加 1 ，开销为 1 ，nums 变为 [3,4,3,3,5] 。
将 nums[0] 和 nums[2] 同时增加 1 ，开销为 1 ，nums 变为 [4,4,4,3,5] 。
将 nums[0] 和 nums[3] 同时增加 1 ，开销为 1 ，nums 变为 [5,4,4,4,5] 。
将 nums[1] 和 nums[2] 同时增加 1 ，开销为 1 ，nums 变为 [5,5,5,4,5] 。
将 nums[3] 增加 1 ，开销为 2 ，nums 变为 [5,5,5,5,5] 。
总开销为 6 。

示例 3：

输入：nums = [3,5,3], cost1 = 1, cost2 = 3

输出：4

解释：

执行以下操作可以使数组中所有元素相等：

将 nums[0] 增加 1 ，开销为 1 ，nums 变为 [4,5,3] 。
将 nums[0] 增加 1 ，开销为 1 ，nums 变为 [5,5,3] 。
将 nums[2] 增加 1 ，开销为 1 ，nums 变为 [5,5,4] 。
将 nums[2] 增加 1 ，开销为 1 ，nums 变为 [5,5,5] 。
总开销为 4 。

 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= cost1 <= 106
1 <= cost2 <= 106

"""

class Solution:
    MODS = 10 ** 9 + 7
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        M = len(nums)
        max_v = max(nums)
        c = sorted([max_v - ii for ii in nums if ii != max_v])
        N = len(c)
        if N == 0:
            return 0
        if cost1 * 2 <= cost2:
            return sum(c) * cost1 % self.MODS

        x, y = c[-1], sum(c[:-1]) if N > 1 else 0
        # print(c, x, y)
        if x <= y:
            res = (x + y) // 2 * cost2 + (x + y) % 2 * cost1
            k = 1
            while True:
                now = (x + y + M * k) // 2 * cost2 + (x + y + M * k) % 2 * cost1
                # print(now)
                if now > res:
                    break
                res = now
                k += 2
            return res % self.MODS
        k = 0
        res = y * cost2 + (x - y) * cost1
        k = 1
        while True:
            xx = x + k
            yy = y + (M - 1) * k
            if xx <= yy:
                now = (xx + yy) // 2 * cost2 + (xx + yy) % 2 * cost1
            else:
                now = yy * cost2 + (xx - yy) * cost1
            if now > res:
                break
            res = now
            k += 1
        return res % self.MODS
        