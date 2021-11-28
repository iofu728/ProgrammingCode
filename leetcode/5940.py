# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-11-28 11:31:39
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-11-28 11:31:51

"""
5940. 从数组中移除最大值和最小值 显示英文描述 
User Accepted:78
User Tried:83
Total Accepted:79
Total Submissions:84
Difficulty:Medium
给你一个下标从 0 开始的数组 nums ，数组由若干 互不相同 的整数组成。

nums 中有一个值最小的元素和一个值最大的元素。分别称为 最小值 和 最大值 。你的目标是从数组中移除这两个元素。

一次 删除 操作定义为从数组的 前面 移除一个元素或从数组的 后面 移除一个元素。

返回将数组中最小值和最大值 都 移除需要的最小删除次数。

 

示例 1：

输入：nums = [2,10,7,5,4,1,8,6]
输出：5
解释：
数组中的最小元素是 nums[5] ，值为 1 。
数组中的最大元素是 nums[1] ，值为 10 。
将最大值和最小值都移除需要从数组前面移除 2 个元素，从数组后面移除 3 个元素。
结果是 2 + 3 = 5 ，这是所有可能情况中的最小删除次数。
示例 2：

输入：nums = [0,-4,19,1,8,-2,-3,5]
输出：3
解释：
数组中的最小元素是 nums[1] ，值为 -4 。
数组中的最大元素是 nums[2] ，值为 19 。
将最大值和最小值都移除需要从数组前面移除 3 个元素。
结果是 3 ，这是所有可能情况中的最小删除次数。 
示例 3：

输入：nums = [101]
输出：1
解释：
数组中只有这一个元素，那么它既是数组中的最小值又是数组中的最大值。
移除它只需要 1 次删除操作。
 

提示：

1 <= nums.length <= 105
-105 <= nums[i] <= 105
nums 中的整数 互不相同
"""
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1
        max_v, min_v = max(nums), min(nums)
        max_idx, min_idx = 0, 0
        for ii, jj in enumerate(nums):
            if jj == max_v:
                max_idx = ii
            if jj == min_v:
                min_idx = ii
        # print(max_idx, min_idx)
        gap1 = min(max_idx + 1, N - max_idx)
        gap2 = min(min_idx + 1, N - min_idx)
        if gap1 > gap2:
            max_idx, min_idx = min_idx, max_idx
            gap1, gap2 = gap2, gap1
        # print(gap1, gap2)
        return gap1 + min(gap2, abs(max_idx - min_idx))
        
        