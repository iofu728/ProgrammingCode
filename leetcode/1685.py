# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2022-01-18 20:09:54
# @Last Modified by:   gunjianpan
# @Last Modified time: 2022-01-18 20:10:04

"""
1685. 有序数组中差绝对值之和
给你一个 非递减 有序整数数组 nums 。

请你建立并返回一个整数数组 result，它跟 nums 长度相同，且result[i] 等于 nums[i] 与数组中所有其他元素差的绝对值之和。

换句话说， result[i] 等于 sum(|nums[i]-nums[j]|) ，其中 0 <= j < nums.length 且 j != i （下标从 0 开始）。

 

示例 1：

输入：nums = [2,3,5]
输出：[4,3,5]
解释：假设数组下标从 0 开始，那么
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4，
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3，
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5。
示例 2：

输入：nums = [1,4,6,8,10]
输出：[24,15,13,15,21]
 

提示：

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
通过次数4,328提交次数7,037
"""
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        a = sum([nums[ii] - nums[0] for ii in range(N)])
        res = [a]
        for ii in range(1, N):
            a = a - (nums[ii] - nums[ii - 1]) * (max(0, N - ii - 1) - max(ii - 1, 0))
            res.append(a)
        return res
