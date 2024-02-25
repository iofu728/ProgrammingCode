# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2024-02-25 23:58:11
# @Last Modified by:   gunjianpan
# @Last Modified time: 2024-02-25 23:58:20

"""
100224. 分割数组 显示英文描述 
通过的用户数0
尝试过的用户数0
用户总通过次数0
用户总提交次数0
题目难度Easy
给你一个长度为 偶数 的整数数组 nums 。你需要将这个数组分割成 nums1 和 nums2 两部分，要求：

nums1.length == nums2.length == nums.length / 2 。
nums1 应包含 互不相同 的元素。
nums2也应包含 互不相同 的元素。
如果能够分割数组就返回 true ，否则返回 false 。

 

示例 1：

输入：nums = [1,1,2,2,3,4]
输出：true
解释：分割 nums 的可行方案之一是 nums1 = [1,2,3] 和 nums2 = [1,2,4] 。
示例 2：

输入：nums = [1,1,1,1]
输出：false
解释：分割 nums 的唯一可行方案是 nums1 = [1,1] 和 nums2 = [1,1] 。但 nums1 和 nums2 都不是由互不相同的元素构成。因此，返回 false 。
 

提示：

1 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
"""
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for i, j in c.items():
            if j > 2:
                return False
        return True