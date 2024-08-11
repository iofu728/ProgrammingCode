# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-08-11 11:33:40
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-08-11 11:33:52

"""
100395. 单调数组对的数目 I 显示英文描述 
通过的用户数22
尝试过的用户数30
用户总通过次数24
用户总提交次数37
题目难度Hard
给你一个长度为 n 的 正 整数数组 nums 。

如果两个 非负 整数数组 (arr1, arr2) 满足以下条件，我们称它们是 单调 数组对：

两个数组的长度都是 n 。
arr1 是单调 非递减 的，换句话说 arr1[0] <= arr1[1] <= ... <= arr1[n - 1] 。
arr2 是单调 非递增 的，换句话说 arr2[0] >= arr2[1] >= ... >= arr2[n - 1] 。
对于所有的 0 <= i <= n - 1 都有 arr1[i] + arr2[i] == nums[i] 。
请你返回所有 单调 数组对的数目。

由于答案可能很大，请你将它对 109 + 7 取余 后返回。

 

示例 1：

输入：nums = [2,3,2]

输出：4

解释：

单调数组对包括：

([0, 1, 1], [2, 2, 1])
([0, 1, 2], [2, 2, 0])
([0, 2, 2], [2, 1, 0])
([1, 2, 2], [1, 1, 0])
示例 2：

输入：nums = [5,5,5,5]

输出：126

 

提示：

1 <= n == nums.length <= 2000
1 <= nums[i] <= 50
"""

MOD = 10**9 + 7
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)

        # Precompute the number of ways to split each number into two parts
        ways_to_split = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        for i in range(max_val + 1):
            for j in range(i + 1):
                ways_to_split[i][j] = 1

        # Dynamic programming to count valid combinations
        dp = [[0] * (max_val + 1) for _ in range(n)]
        for i in range(nums[0] + 1):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(nums[i] + 1):
                for k in range(j, nums[i - 1] + 1):
                    if nums[i] - j = nums[i - 1] - k:
                        dp[i][j] = (dp[i][j] + dp[i - 1][k] * ways_to_split[nums[i]][j]) % MOD

        # Sum up all the valid combinations
        return sum(dp[-1]) % MOD
