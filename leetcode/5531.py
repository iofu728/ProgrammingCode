# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2020-10-04 10:30:21
# @Last Modified by:   gunjianpan
# @Last Modified time: 2020-10-04 10:35:07

"""
5531. 特殊数组的特征值 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。

注意： x 不必 是 nums 的中的元素。

如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。

 

示例 1：

输入：nums = [3,5]
输出：2
解释：有 2 个元素（3 和 5）大于或等于 2 。
示例 2：

输入：nums = [0,0]
输出：-1
解释：没有满足题目要求的特殊数组，故而也不存在特征值 x 。
如果 x = 0，应该有 0 个元素 >= x，但实际有 2 个。
如果 x = 1，应该有 1 个元素 >= x，但实际有 0 个。
如果 x = 2，应该有 2 个元素 >= x，但实际有 0 个。
x 不能取更大的值，因为 nums 中只有两个元素。
示例 3：

输入：nums = [0,4,3,0,4]
输出：3
解释：有 3 个元素大于或等于 3 。
示例 4：

输入：nums = [3,6,7,7,0]
输出：-1
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
import bisect


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        N = len(nums)
        for ii in range(0, nums[-1] + 1):
            idx = bisect.bisect_left(nums, ii)
            # print(idx, ii)
            if N - idx == ii:
                return ii
        return -1
