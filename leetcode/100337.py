# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-06-23 16:19:32
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-06-23 16:19:41

"""
100337. 最大化子数组的总成本 显示英文描述 
通过的用户数4
尝试过的用户数12
用户总通过次数4
用户总提交次数15
题目难度Medium
给你一个长度为 n 的整数数组 nums。

子数组 nums[l..r]（其中 0 <= l <= r < n）的 成本 定义为：

cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)r − l

你的任务是将 nums 分割成若干子数组，使得所有子数组的成本之和 最大化，并确保每个元素 正好 属于一个子数组。

具体来说，如果 nums 被分割成 k 个子数组，且分割点为索引 i1, i2, ..., ik − 1（其中 0 <= i1 < i2 < ... < ik - 1 < n - 1），则总成本为：

cost(0, i1) + cost(i1 + 1, i2) + ... + cost(ik − 1 + 1, n − 1)

返回在最优分割方式下的子数组成本之和的最大值。

注意：如果 nums 没有被分割，即 k = 1，则总成本即为 cost(0, n - 1)。

 

示例 1：

输入： nums = [1,-2,3,4]

输出： 10

解释：

一种总成本最大化的方法是将 [1, -2, 3, 4] 分割成子数组 [1, -2, 3] 和 [4]。总成本为 (1 + 2 + 3) + 4 = 10。

示例 2：

输入： nums = [1,-1,1,-1]

输出： 4

解释：

一种总成本最大化的方法是将 [1, -1, 1, -1] 分割成子数组 [1, -1] 和 [1, -1]。总成本为 (1 + 1) + (1 + 1) = 4。

示例 3：

输入： nums = [0]

输出： 0

解释：

无法进一步分割数组，因此答案为 0。

示例 4：

输入： nums = [1,-1]

输出： 2

解释：

选择整个数组，总成本为 1 + 1 = 2，这是可能的最大成本。

 

提示：

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        res = 0
        dp = [-float("inf"), -float("inf")]
        for jj, ii in enumerate(nums):
            now = [-float("inf"), -float("inf")]
            if jj == 0:
                now[1] = ii
                # now[0] = 0
            else:
                now[1] = max(dp) + ii
                now[0] = dp[1] - ii
            # print(dp)
            dp = now
            
        return max(dp)