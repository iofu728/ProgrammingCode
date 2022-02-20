# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-02-19 14:13:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-02-19 14:13:51

"""
1755. 最接近目标值的子序列和
给你一个整数数组 nums 和一个目标值 goal 。

你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum - goal) 。

返回 abs(sum - goal) 可能的 最小值 。

注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。

 

示例 1：

输入：nums = [5,-7,3,5], goal = 6
输出：0
解释：选择整个数组作为选出的子序列，元素和为 6 。
子序列和与目标值相等，所以绝对差为 0 。
示例 2：

输入：nums = [7,-9,15,-2], goal = -5
输出：1
解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
示例 3：

输入：nums = [1,2,3], goal = -7
输出：7
 

提示：

1 <= nums.length <= 40
-107 <= nums[i] <= 107
-109 <= goal <= 109
通过次数3,630提交次数8,518
"""


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def get_sum(nums):
            res = {0}
            for ii in nums:
                res |= {ii + i for i in res}
            return sorted(list(res))

        N = len(nums)
        left, right = get_sum(nums[: N // 2]), get_sum(nums[N // 2 :])
        N1, N2 = len(left), len(right)
        res = 10 ** 9 + 7
        ii, jj = 0, N2 - 1
        while ii < N1 and jj >= 0:
            res = min(res, abs(left[ii] + right[jj] - goal))
            if left[ii] + right[jj] - goal >= 0:
                jj -= 1
            else:
                ii += 1
        return res
