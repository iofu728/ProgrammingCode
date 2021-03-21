# -*- coding: utf-8 -*-
# @Author: gunjianpan
# @Date:   2021-03-21 10:38:20
# @Last Modified by:   gunjianpan
# @Last Modified time: 2021-03-21 10:38:30

'''
5709. 最大升序子数组和 显示英文描述 
通过的用户数667
尝试过的用户数741
用户总通过次数668
用户总提交次数791
题目难度Easy
给你一个正整数组成的数组 nums ，返回 nums 中一个 升序 子数组的最大可能元素和。

子数组是数组中的一个连续数字序列。

已知子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，若对所有 i（l <= i < r），numsi < numsi+1 都成立，则称这一子数组为 升序 子数组。注意，大小为 1 的子数组也视作 升序 子数组。

 

示例 1：

输入：nums = [10,20,30,5,10,50]
输出：65
解释：[5,10,50] 是元素和最大的升序子数组，最大元素和为 65 。
示例 2：

输入：nums = [10,20,30,40,50]
输出：150
解释：[10,20,30,40,50] 是元素和最大的升序子数组，最大元素和为 150 。 
示例 3：

输入：nums = [12,17,15,13,10,11,12]
输出：33
解释：[10,11,12] 是元素和最大的升序子数组，最大元素和为 33 。 
示例 4：

输入：nums = [100,10,1]
输出：100
 

提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N = len(nums)
        dp = nums.copy()
        for ii in range(1, N):
            if nums[ii - 1] < nums[ii]:
                dp[ii] = max(dp[ii], dp[ii - 1] + nums[ii])
        # print(dp)
        return max(dp)