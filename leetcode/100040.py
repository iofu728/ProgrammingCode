# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2023-09-17 10:36:35
# @Last Modified by:   gunjianpan
# @Last Modified time: 2023-09-17 12:09:25

"""
100040. 让所有学生保持开心的分组方法数 显示英文描述 
通过的用户数19
尝试过的用户数28
用户总通过次数20
用户总提交次数37
题目难度Medium
给你一个下标从 0 开始、长度为 n 的整数数组 nums ，其中 n 是班级中学生的总数。班主任希望能够在让所有学生保持开心的情况下选出一组学生：

如果能够满足下述两个条件之一，则认为第 i 位学生将会保持开心：

这位学生被选中，并且被选中的学生人数 严格大于 nums[i] 。
这位学生没有被选中，并且被选中的学生人数 严格小于 nums[i] 。
返回能够满足让所有学生保持开心的分组方法的数目。

 

示例 1：

输入：nums = [1,1]
输出：2
解释：
有两种可行的方法：
班主任没有选中学生。
班主任选中所有学生形成一组。 
如果班主任仅选中一个学生来完成分组，那么两个学生都无法保持开心。因此，仅存在两种可行的方法。
示例 2：

输入：nums = [6,0,3,3,6,7,2,7]
输出：3
解释：
存在三种可行的方法：
班主任选中下标为 1 的学生形成一组。
班主任选中下标为 1、2、3、6 的学生形成一组。
班主任选中所有学生形成一组。 
 

提示：

1 <= nums.length <= 105
0 <= nums[i] < nums.length
"""
class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        i = 0
        if nums[0] > 0:
            res += 1
        while i < len(nums):
            if i + 1 > nums[i] and (i == len(nums) - 1 or i + 1 < nums[i + 1]):
                res += 1
            i += 1
        return res