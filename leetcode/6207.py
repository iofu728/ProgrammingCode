# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-10-16 12:26:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-10-16 12:26:32

"""
6207. 统计定界子数组的数目 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Hard
给你一个整数数组 nums 和两个整数 minK 以及 maxK 。

nums 的定界子数组是满足下述条件的一个子数组：

子数组中的 最小值 等于 minK 。
子数组中的 最大值 等于 maxK 。
返回定界子数组的数目。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [1,3,5,2,7,5], minK = 1, maxK = 5
输出：2
解释：定界子数组是 [1,3,5] 和 [1,3,5,2] 。
示例 2：

输入：nums = [1,1,1,1], minK = 1, maxK = 1
输出：10
解释：nums 的每个子数组都是一个定界子数组。共有 10 个子数组。
 

提示：

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
"""
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        res, left = 0, 0
        pos1, pos2 = -1, -1
        for right in range(n):
            if nums[right] == minK:
                pos1 = right
            if nums[right] == maxK:
                pos2 = right
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
            res += max(0, min(pos1, pos2) - left + 1)

        return res
        