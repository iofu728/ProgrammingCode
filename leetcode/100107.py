# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-10-29 11:44:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-10-29 11:45:05

"""
100107. 使数组变美的最小增量运算数 显示英文描述 
通过的用户数30
尝试过的用户数60
用户总通过次数32
用户总提交次数79
题目难度Medium
给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和一个整数 k 。

你可以执行下述 递增 运算 任意 次（可以是 0 次）：

从范围 [0, n - 1] 中选则一个下标 i ，并将 nums[i] 的值加 1 。
如果数组中任何长度 大于或等于 3 的子数组，其 最大 元素都大于或等于 k ，则认为数组是一个 美丽数组 。

以整数形式返回使数组变为 美丽数组 需要执行的 最小 递增运算数。

子数组是数组中的一个连续 非空 元素序列。

 

示例 1：

输入：nums = [2,3,0,0,2], k = 4
输出：3
解释：可以执行下述递增运算，使 nums 变为美丽数组：
选择下标 i = 1 ，并且将 nums[1] 的值加 1 -> [2,4,0,0,2] 。
选择下标 i = 4 ，并且将 nums[4] 的值加 1 -> [2,4,0,0,3] 。
选择下标 i = 4 ，并且将 nums[4] 的值加 1 -> [2,4,0,0,4] 。
长度大于或等于 3 的子数组为 [2,4,0], [4,0,0], [0,0,4], [2,4,0,0], [4,0,0,4], [2,4,0,0,4] 。
在所有子数组中，最大元素都等于 k = 4 ，所以 nums 现在是美丽数组。
可以证明无法用少于 3 次递增运算使 nums 变为美丽数组。
因此，答案为 3 。
示例 2：

输入：nums = [0,1,3,3], k = 5
输出：2
解释：可以执行下述递增运算，使 nums 变为美丽数组：
选择下标 i = 2 ，并且将 nums[2] 的值加 1 -> [0,1,4,3] 。
选择下标 i = 2 ，并且将 nums[2] 的值加 1 -> [0,1,5,3] 。
长度大于或等于 3 的子数组为 [0,1,5]、[1,5,3]、[0,1,5,3] 。
在所有子数组中，最大元素都等于 k = 5 ，所以 nums 现在是美丽数组。
可以证明无法用少于 2 次递增运算使 nums 变为美丽数组。 
因此，答案为 2 。
示例 3：

输入：nums = [1,1,2], k = 1
输出：0
解释：在这个示例中，只有一个长度大于或等于 3 的子数组 [1,1,2] 。
其最大元素 2 已经大于 k = 1 ，所以无需执行任何增量运算。
因此，答案为 0 。
 

提示：

3 <= n == nums.length <= 105
0 <= nums[i] <= 109
0 <= k <= 109
"""
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        def get_c(j):
            return 0 if nums[j] >= k else k - nums[j]
        @lru_cache(None)
        def dfs(i, c=1):
            res = float("inf")
            if i >= N:
                return 0
            for idx in range(max(0, i - 2), min(i + c, N)):
                t = idx + 3
                now = idx + 1
                while now < N and now < t:
                    if nums[now] >= k:
                        t = now + 3
                    now += 1
                res = min(get_c(idx) + dfs(t), res)
            # print(i, res)
            return res
        N = len(nums)
        return dfs(0, 3)
                
            