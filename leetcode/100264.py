'''
100264. 最长的严格递增或递减子数组 显示英文描述
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个整数数组 nums 。

返回数组 nums 中 严格递增 或 严格递减 的最长非空子数组的长度。



示例 1：

输入：nums = [1,4,3,3,2]

输出：2

解释：

nums 中严格递增的子数组有[1]、[2]、[3]、[3]、[4] 以及 [1,4] 。

nums 中严格递减的子数组有[1]、[2]、[3]、[3]、[4]、[3,2] 以及 [4,3] 。

因此，返回 2 。

示例 2：

输入：nums = [3,3,3,3]

输出：1

解释：

nums 中严格递增的子数组有 [3]、[3]、[3] 以及 [3] 。

nums 中严格递减的子数组有 [3]、[3]、[3] 以及 [3] 。

因此，返回 1 。

示例 3：

输入：nums = [3,2,1]

输出：3

解释：

nums 中严格递增的子数组有 [3]、[2] 以及 [1] 。

nums 中严格递减的子数组有 [3]、[2]、[1]、[3,2]、[2,1] 以及 [3,2,1] 。

因此，返回 3 。



提示：

1 <= nums.length <= 50
1 <= nums[i] <= 50
'''
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        a, b = 1, 1
        for ii in range(1, len(nums)):
            if nums[ii] > nums[ii - 1]:
                a += 1
                b = 1
            elif nums[ii] < nums[ii - 1]:
                a = 1
                b += 1
            else:
                a, b = 1, 1
            res = max(res, a, b)
        return res
