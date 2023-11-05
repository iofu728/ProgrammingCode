# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-11-05 13:39:17
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-11-05 13:39:27

"""
100112. 平衡子序列的最大和 显示英文描述 
通过的用户数12
尝试过的用户数27
用户总通过次数12
用户总提交次数48
题目难度Hard
给你一个下标从 0 开始的整数数组 nums 。

nums 一个长度为 k 的 子序列 指的是选出 k 个 下标 i0 < i1 < ... < ik-1 ，如果这个子序列满足以下条件，我们说它是 平衡的 ：

对于范围 [1, k - 1] 内的所有 j ，nums[ij] - nums[ij-1] >= ij - ij-1 都成立。
nums 长度为 1 的 子序列 是平衡的。

请你返回一个整数，表示 nums 平衡 子序列里面的 最大元素和 。

一个数组的 子序列 指的是从原数组中删除一些元素（也可能一个元素也不删除）后，剩余元素保持相对顺序得到的 非空 新数组。

 

示例 1：

输入：nums = [3,3,5,6]
输出：14
解释：这个例子中，选择子序列 [3,5,6] ，下标为 0 ，2 和 3 的元素被选中。
nums[2] - nums[0] >= 2 - 0 。
nums[3] - nums[2] >= 3 - 2 。
所以，这是一个平衡子序列，且它的和是所有平衡子序列里最大的。
包含下标 1 ，2 和 3 的子序列也是一个平衡的子序列。
最大平衡子序列和为 14 。
示例 2：

输入：nums = [5,-1,-3,8]
输出：13
解释：这个例子中，选择子序列 [5,8] ，下标为 0 和 3 的元素被选中。
nums[3] - nums[0] >= 3 - 0 。
所以，这是一个平衡子序列，且它的和是所有平衡子序列里最大的。
最大平衡子序列和为 13 。
示例 3：

输入：nums = [-2,-1]
输出：-1
解释：这个例子中，选择子序列 [-1] 。
这是一个平衡子序列，而且它的和是 nums 所有平衡子序列里最大的。
 

提示：

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        to_ret = nums[0]
        values = [[-1e99, 0]]
        for i in range(len(nums)) :
            vt = nums[i] - i
            pt = bisect.bisect(values, [vt+0.1, 0])
            sumt = nums[i]
            if nums[i] >= 0 :
                if pt > 0 :
                    sumt += values[pt-1][1]
                values.insert(pt, [vt, sumt])
                while pt + 1 < len(values) and values[pt+1][1] <=  values[pt][1] :
                    values.pop(pt+1)
            to_ret = max(to_ret, sumt)
            # print(values)
        return to_ret