# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-08-30 10:37:36
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-08-30 10:56:28

"""
5500. 乘积为正数的最长子数组长度 显示英文描述 
通过的用户数286
尝试过的用户数477
用户总通过次数287
用户总提交次数733
题目难度Medium
给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

请你返回乘积为正数的最长子数组长度。

 

示例  1：

输入：nums = [1,-2,-3,4]
输出：4
解释：数组本身乘积就是正数，值为 24 。
示例 2：

输入：nums = [0,1,-2,-3,-4]
输出：3
解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
示例 3：

输入：nums = [-1,-2,-3,0,1]
输出：2
解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
示例 4：

输入：nums = [-1,2]
输出：1
示例 5：

输入：nums = [1,2,3,5,-6,4,0,10]
输出：4
 

提示：

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0] * 2 for _ in range(N + 1)]
        res = 0
        for ii in range(N):
            if nums[ii] > 0:
                dp[ii + 1][0] = dp[ii][0] + 1
                dp[ii + 1][1] = dp[ii][1] + 1 if dp[ii][1] else dp[ii][1]
            elif nums[ii] < 0:
                dp[ii + 1][0] = dp[ii][1] + 1 if dp[ii][1] else 0
                dp[ii + 1][1] = dp[ii][0] + 1
                res = max(dp[ii][0], res)
            else:
                res = max(dp[ii][0], res)
        return max(dp[N][0], res)
