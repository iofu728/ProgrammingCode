# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-20 11:16:43
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-20 11:16:54

"""
6467. 找出最长等值子数组 显示英文描述 
通过的用户数181
尝试过的用户数293
用户总通过次数196
用户总提交次数474
题目难度Medium
给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。

如果子数组中所有元素都相等，则认为子数组是一个 等值子数组 。注意，空数组是 等值子数组 。

从 nums 中删除最多 k 个元素后，返回可能的最长等值子数组的长度。

子数组 是数组中一个连续且可能为空的元素序列。

 

示例 1：

输入：nums = [1,3,2,3,1,3], k = 3
输出：3
解释：最优的方案是删除下标 2 和下标 4 的元素。
删除后，nums 等于 [1, 3, 3, 3] 。
最长等值子数组从 i = 1 开始到 j = 3 结束，长度等于 3 。
可以证明无法创建更长的等值子数组。
示例 2：

输入：nums = [1,1,2,2,1,1], k = 2
输出：4
解释：最优的方案是删除下标 2 和下标 3 的元素。 
删除后，nums 等于 [1, 1, 1, 1] 。 
数组自身就是等值子数组，长度等于 4 。 
可以证明无法创建更长的等值子数组。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= nums.length
0 <= k <= nums.length
"""
class Solution:
    def longestEqualSubarray(self, nums: List[int], kk: int) -> int:
        z = defaultdict(list)
        for i, j in enumerate(nums):
            z[j].append(i)
        z = {k: [j - i for i, j in enumerate(v)] for k, v in z.items()}
        res = 0
        # print(z)
        for k, v in z.items():
            for r in range(len(v) - 1, -1, -1):
                idx = bisect.bisect_left(v, v[r] - kk)
                # print(v, r, idx, v[r], kk)
                res = max(res, r - idx + 1)
        return res
                