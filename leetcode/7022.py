# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-08-13 11:19:41
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-08-13 11:20:03

"""
7022. 限制条件下元素之间的最小绝对差 显示英文描述 
通过的用户数1
尝试过的用户数6
用户总通过次数1
用户总提交次数9
题目难度Medium
给你一个下标从 0 开始的整数数组 nums 和一个整数 x 。

请你找到数组中下标距离至少为 x 的两个元素的 差值绝对值 的 最小值 。

换言之，请你找到两个下标 i 和 j ，满足 abs(i - j) >= x 且 abs(nums[i] - nums[j]) 的值最小。

请你返回一个整数，表示下标距离至少为 x 的两个元素之间的差值绝对值的 最小值 。

 

示例 1：

输入：nums = [4,3,2,4], x = 2
输出：0
解释：我们选择 nums[0] = 4 和 nums[3] = 4 。
它们下标距离满足至少为 2 ，差值绝对值为最小值 0 。
0 是最优解。
示例 2：

输入：nums = [5,3,2,10,15], x = 1
输出：1
解释：我们选择 nums[1] = 3 和 nums[2] = 2 。
它们下标距离满足至少为 1 ，差值绝对值为最小值 1 。
1 是最优解。
示例 3：

输入：nums = [1,2,3,4], x = 3
输出：3
解释：我们选择 nums[0] = 1 和 nums[3] = 4 。
它们下标距离满足至少为 3 ，差值绝对值为最小值 3 。
3 是最优解。
 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= x < nums.length
"""
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        q = []
        res = float("inf")
        N = len(nums)
        for ii in range(x, N):
            bisect.insort(q, nums[ii - x])
            idx = bisect.bisect_left(q, nums[ii])
            if 0 <= idx < len(q):
                res = min(res, abs(q[idx] - nums[ii]))
            if 0 <= idx - 1 < len(q):
                res = min(res, abs(q[idx - 1] - nums[ii]))
        return res
        