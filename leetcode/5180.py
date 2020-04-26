# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-04-26 13:19:34
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-04-26 13:27:47

"""
5180. 带限制的子序列和 显示英文描述 
通过的用户数260
尝试过的用户数491
用户总通过次数278
用户总提交次数1119
题目难度Hard
给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。

数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。

示例 1：

输入：nums = [10,2,-10,5,20], k = 2
输出：37
解释：子序列为 [10, 2, 5, 20] 。
示例 2：

输入：nums = [-1,-2,-3], k = 1
输出：-1
解释：子序列必须是非空的，所以我们选择最大的数字。
示例 3：

输入：nums = [10,-2,-10,-5,20], k = 2
输出：23
解释：子序列为 [10, -2, -5, 20] 。
 

提示：

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [ii for idx, ii in enumerate(nums)]
        pre = []
        heapq.heappush(pre, (-nums[0], 0))
        for ii in range(1, N):
            res, res_id = heapq.heappop(pre)
            while ii - res_id > k:
                # print(res, res_id)
                res, res_id = heapq.heappop(pre)
            heapq.heappush(pre, (res, res_id))
            res = -res
            dp[ii] = dp[ii] + (0 if res < 0 else res)
            heapq.heappush(pre, (-dp[ii], ii))

        return max(dp)

