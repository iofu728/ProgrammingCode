# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-10-12 22:56:55
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-10-12 22:57:06

"""
2875. 无限数组的最短子数组 显示英文描述 
通过的用户数936
尝试过的用户数1450
用户总通过次数983
用户总提交次数4384
题目难度Medium
给你一个下标从 0 开始的数组 nums 和一个整数 target 。

下标从 0 开始的数组 infinite_nums 是通过无限地将 nums 的元素追加到自己之后生成的。

请你从 infinite_nums 中找出满足 元素和 等于 target 的 最短 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 -1 。

 

示例 1：

输入：nums = [1,2,3], target = 5
输出：2
解释：在这个例子中 infinite_nums = [1,2,3,1,2,3,1,2,...] 。
区间 [1,2] 内的子数组的元素和等于 target = 5 ，且长度 length = 2 。
可以证明，当元素和等于目标值 target = 5 时，2 是子数组的最短长度。
示例 2：

输入：nums = [1,1,1,2,3], target = 4
输出：2
解释：在这个例子中 infinite_nums = [1,1,1,2,3,1,1,1,2,3,1,1,...].
区间 [4,5] 内的子数组的元素和等于 target = 4 ，且长度 length = 2 。
可以证明，当元素和等于目标值 target = 4 时，2 是子数组的最短长度。
示例 3：

输入：nums = [2,4,6,8], target = 3
输出：-1
解释：在这个例子中 infinite_nums = [2,4,6,8,2,4,6,8,...] 。
可以证明，不存在元素和等于目标值 target = 3 的子数组。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= target <= 109
"""
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        S, N = sum(nums), len(nums)
        z = (target // S) * N
        target %= S
        # print(target)
        if target == 0:
            return z
        if min(nums) > target:
            return -1
        if all(ii % 2 == 0 for ii in nums) and target % 2 == 1:
            return -1


        g = {0: -1}
        pre = 0
        res = N + 1
        for ii in range(2 * N):
            now = nums[ii % N]
            pre += now
            # print(pre, g, target)
            if pre - target in g:
                res = min(res, ii - g[pre - target])
            g[pre] = ii
        return res + z if res != N + 1 else -1
            